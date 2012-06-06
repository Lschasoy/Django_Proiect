from django.db import models
from django.contrib.auth.models import User
import md5
import hashlib
from django import forms
import factory


class Usuario(models.Model):
	name= models.CharField(blank = False, unique = True, null = False, max_length= 50)
	email= models.EmailField(max_length= 50)
	password= models.CharField(max_length= 50)
	create_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	#gravatar_img = models.URLField(max_length=200)
	
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
		n = Usuario.objects.filter(name=userName)
		if n:
			raise ValueError ('Elija un nombre distinto')
		u = Usuario()
		if ((u.long_p(userPass)==True) & (u.short_p(userPass)==True) ):#& (u.confirm_p(userPass) == True)):
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
			raise ValueError('Introduzca contrasena.')
		usuario = Usuario()	
		usuario = Usuario.objects.filter(name = userName)
		if usuario:
			usuario = Usuario.objects.get(name = userName)
			paw = hashlib.new('sha1')
			paw.update(str(userPass))
			pa = paw.hexdigest()
			if (str(usuario.password) == str(pa)):
				return True
			else:
				return False
		else:
			return False

class UserFactory(factory.Factory):
	FACTORY_FOR = Usuario

	name = factory.sequence(lambda a: 'Marcos{0}'.format(a))
	email =  factory.sequence(lambda n: 'correo{0}@example.com'.format(n))
	password = factory.sequence(lambda e: 'random{0}'.format(e))


class Micropost(models.Model):
	texto = models.CharField(max_length= 140)
	create_at= models.DateTimeField(auto_now_add=True)
	resumen = models.ManyToManyField(Usuario, through='ResumenMicro')
	
	def __unicode__(self):
		return self.texto
		
	def create_post(self,id_Usuario,text):
		#print "Id: ", id_Usuario
		micro = Micropost(texto=text)
		micro.save()
		resumen = ResumenMicro()
		resumen.create_resumen(id_Usuario,micro.id)

class MicropostFactory(factory.Factory):
	FACTORY_FOR = Micropost

	texto = factory.Sequence(lambda n: 'Este es mi post numero{0}'.format(n))

	

class ResumenMicro(models.Model):
	id_Usuario = models.ForeignKey(Usuario)
	id_Micropost = models.ForeignKey(Micropost)

	def create_resumen (self,id_User,id_Micro):
		usuario = Usuario()
		usuario = Usuario.objects.get(id = id_User)
		micro = Micropost()
		micro = Micropost.objects.get(id = id_Micro)
		resumen = ResumenMicro( id_Usuario=usuario, id_Micropost=micro )
		resumen.save()
		
class Amigo (models.Model):
	id_Usuario = models.ForeignKey(Usuario, related_name="id_Usuario")
	id_Amigo = models.ForeignKey(Usuario, related_name="id_Amigo")
	create_at= models.DateTimeField(auto_now_add=True)

	def create_amigo(self,id_Usuario,id_Amigo):
		usuario = Usuario()
		usuario = Usuario.objects.get(id = id_Usuario)
		amigo = Usuario()
		amigo = Usuario.objects.get(id = id_Amigo)
		resumen = Amigo( id_Usuario=usuario, id_Amigo=amigo )
		resumen.save()
	
	
	
	
	
	
