from django.db import models
from django.contrib import auth
from django.contrib.auth.hashers import (
	check_password, is_password_usable)

class Usuario(models.Model):
	nombre = models.CharField(max_length= 50)
	email = models.EmailField(max_length= 50)
	password = models.EmailField(max_length= 50)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
