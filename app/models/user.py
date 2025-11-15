from django.db import models
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from .house import BaseModel

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email=None,password = None ,**extra_fields):
        if not phone_number:
            raise ValueError('Phone_number maydoni bo`lishi kerak emas!')
        # phone_number = self.normalize_phone_number(phone_number)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        
        user.set_password(password or '123456')
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, email=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser is_admin=True bo`lishi kerak!')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bo`lishi kerak!')

        return self.create_user(phone_number, email, password, **extra_fields)


class User(BaseModel,AbstractBaseUser, PermissionsMixin):
    # phone_regex = RegexValidator(
    #     regex=r'^\+998\d{9}$',
    #     message="Telefon raqam '+998XXXXXXXXX' formatida bo'lishi kerak!"
    # )
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(unique=True, default=None)
    phone_number = models.CharField(max_length=13, unique=True)
    # phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    email_verified = models.BooleanField(default=False)
    call_from = models.TimeField(help_text="Start time when user can receive calls",blank=True,null=True)
    call_to = models.TimeField(help_text="End time when user can receive calls",blank=True,null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.email if self.email else self.phone_number

    @property
    def is_superuser(self):
        return self.is_admin
    
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):  # not hashed yet
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return super().check_password(raw_password)
    

class UserOTP(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    otp_code = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"OTP for {self.user.email} - {'Used' if self.is_used else 'Unused'}"