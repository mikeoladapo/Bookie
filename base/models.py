from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager,PermissionsMixin
from django.core.validators import RegexValidator

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        if extra_fields.get("is_staff") is not True:
            return ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9_]{3,20}$',
        message=(
        "Username must be 3-20 characters long and can only contain letters, "
        "numbers, and underscores."),
        code="invalid username"
        )
    username = models.CharField(max_length=20,unique=True,
                                validators=[username_regex],
                                error_messages={"unique":"username is already taken"})
    email = models.EmailField()
    password = models.CharField()
    profile_picture = models.ImageField(upload_to="profile_picture",null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField("auth.Group",related_name="customuser_set")
    user_permissions = models.ManyToManyField("auth.Permission",related_name="customuser_permissions_set",blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()
    def __str__(self):
        return self.username

class Author(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=30)

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    released_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    picture = models.ImageField(upload_to="book_picture",blank=True,null=True)