from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

__author__ = 'vatsalshah'


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
                                password=password,
                                name=name
                                )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model
    """
    created_at = models.DateTimeField(
        verbose_name='created at',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='updated at',
        auto_now=True
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    name = models.CharField(
        verbose_name='full name',
        max_length=255
    )
    USER_TYPES = (
        ('PA', 'Patient'),
        ('DO', 'Doctor'),
        ('PH', 'Pharmacist')
    )
    user_type = models.CharField(
        verbose_name='user type',
        max_length=2,
        default='PA',
        choices=USER_TYPES
    )
    phone = PhoneNumberField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'User'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.name

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.name.split(' ')[0]

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class MedicalRecord(models.Model):
    """
    User Medical Records
    """
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    user = models.ForeignKey(
        to=User,
        related_name='medicalrecord_user'
    )
    doctor = models.ForeignKey(
        to=User,
        related_name='medicalrecord_doctor'
    )
    diagnosis = models.TextField(blank=True)


class Prescription(models.Model):
    """
    Medicine Prescription
    """
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    user = models.ForeignKey(
        to=User,
        related_name='prescription_user'
    )
    doctor = models.ForeignKey(
        to=User,
        related_name='prescription_doctor'
    )


class Medicine(models.Model):
    """
    Medicine
    """
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    strength = models.IntegerField()
    frequency = models.CharField(max_length=50)
    prescription = models.ForeignKey(
        to=Prescription
    )


class Approval(models.Model):
    """
    Approvals
    """
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    prescription = models.ForeignKey(
        to=Prescription
    )
    user = models.ForeignKey(
        to=User
    )
    STATUS_TYPES = (
        ('PE', 'Pending'),
        ('RE', 'Rejected'),
        ('AP', 'Approved')
    )
    status = models.CharField(
        max_length=2,
        default='PE',
        choices=STATUS_TYPES
    )