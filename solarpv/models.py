from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator
from model_utils import Choices

PREFIX = Choices('Mr', 'Mrs', 'Ms', 'Dr')

class Client(models.Model):
    client_id = models.AutoField(primary_key=True, validators=[MaxValueValidator(999999)])
    client_name = models.CharField(max_length=50)
    client_type = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('client_edit', kwargs={'pk': self.pk})

class User_Manager(BaseUserManager):
    def create_user(self, email, username, prefix, firstname, middlename, lastname, job_title, officephone, cellphone, client, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            prefix=prefix,
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            job_title=job_title,
            officephone=officephone,
            cellphone=cellphone,
            client=client,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, prefix, firstname, middlename, lastname, job_title, officephone, cellphone, client):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            prefix=prefix,
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            job_title=job_title,
            officephone=officephone,
            cellphone=cellphone,
            client=client,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=8, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    prefix = models.CharField(max_length=4, choices=PREFIX, blank=True)
    firstname = models.CharField(verbose_name='First Name', max_length=50, blank=True)
    middlename = models.CharField(verbose_name='Middle Name', max_length=50, blank=True)
    lastname = models.CharField(verbose_name='Last Name', max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    officephone = models.CharField(verbose_name='Office phone', max_length=12, blank=True)
    cellphone = models.CharField(verbose_name='Cell phone', max_length=12, blank=True)
    client = models.ForeignKey(Client, default=100000, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'prefix', 'firstname', 'middlename', 'lastname', 'job_title', 'officephone', 'cellphone', 'client']

    objects = User_Manager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
