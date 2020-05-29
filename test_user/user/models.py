from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser	

class MyManager(BaseUserManager):
	def create_user(self,email,password=None):
		if not email:
			raise ValueError("must have a mail id")
		
		user=self.model(email=self.normalize_email(email),
			)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self,email,password):

		user=self.create_user(email=self.normalize_email(email),
			password=password,
			)
		user.is_admin=True
		user.is_staff=True
		user.is_student=False
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email=models.EmailField(verbose_name='email',max_length=255,unique=True)
	username=models.CharField(max_length=255,unique=True)
	is_admin=models.BooleanField(default=False)
	is_staff=models.BooleanField(default=False)
	semester=models.CharField(max_length=20)
	is_student=models.BooleanField(default=True)

	USERNAME_FIELD='email'
	REQUIRED_FIELD=[]


	objects=MyManager()

	def __str__(self):
		return self.email
	def has_perm(self,perm,obj=None):
		return self.is_admin
	def has_module_perms(self,app_label):
		return True

