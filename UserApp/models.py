from django.db import models
import md5
import hashlib
from django import forms


class Usuario(models.Model):
	
	name= models.CharField(blank = False, unique = True, null = False, max_length= 50)
	email= models.CharField(max_length= 50)
	password= models.CharField(max_length= 50)
	create_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name

	def short_p(step, passw):
		if (len(passw) >= 5):
			return True
		else:
			raise ValueError('El password debe de ser mayor de 5 caracteres.')
			return False
	
	def long_p(step, passw):
		if (len(passw) < 41):
			return True
		else:
			raise ValueError('El password debe de ser menor de 41 caracteres.')
			return False

	def confirm_p(step,passw1):
		passw2 = raw_input("Escriba la confirmacion del password: ")
		if (passw1 == passw2):
			return True
		else:
			raise ValueError('Fallo en la confirmacion del password.')
			return False
	
	def create(self,userName, userEmail, userPass):
		if not userName:
			raise ValueError('EL NOMBRE DE USUARIO, DEBE SER ESTABLECIDO')
		#print "userName: ",userName, "Tipo userName: ",type(userName)
		#print "userEmail: ",userEmail, "Tipo userEmail: ",type(userEmail)
		#print "userPass: ",userPass, "Tipo userPass: ",type(userPass)
		u = Usuario()
		if ((u.long_p(userPass)==True) & (u.short_p(userPass)==True) & (u.confirm_p(userPass) == True)):
				p = hashlib.new('sha1')
				p.update(str(userPass))
				pa = p.hexdigest()
				usuario = Usuario(name=userName, email=userEmail, password=pa)
				usuario.save()
		else:
			raise ValueError('Error Pass')
		return usuario
 
	def authenticate(self, userName, userPass):
		if not userName:
			raise ValueError('Introduzca nombre de usuario.')
		if not userPass:
			raise ValueError('Introduca contrasena.')		
		usuario = Usuario.objects.get(name = userName)
		paw = hashlib.new('sha1')
		paw.update(str(userPass))
		pa = paw.hexdigest()
		if (str(usuario.password) == str(pa)):
			return True
		else:
			return False


class UserForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('name', 'email')

