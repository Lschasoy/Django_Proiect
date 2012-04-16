from django.db import models

class UserManager(models.Manager):

	def create_user(self, name, email=None, password=None):
		if not name:
			raise ValueError('EL NOMBRE DE USUARIO, DEBE SER ESTABLECIDO')
			user = self.model(name=name, email=email, password=password)	
			user.save()
		return user

class Usuario(models.Model):
	name       = models.CharField(max_length= 50)
	email      = models.EmailField(max_length= 50)
	password   = models.CharField(max_length= 50)
	create_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
