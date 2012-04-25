from django.db import models
import md5
import hashlib



class Usuario(models.Model):
	
	name= models.CharField(blank = False, unique = True, null = False, max_length= 50)
	email= models.CharField(max_length= 50)
	password= models.CharField(max_length= 50)
	create_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name


	def create(self,userName, userEmail, userPass):
		if not userName:
			raise ValueError('EL NOMBRE DE USUARIO, DEBE SER ESTABLECIDO')
		#print "userName: ",userName, "Tipo userName: ",type(userName)
		#print "userEmail: ",userEmail, "Tipo userEmail: ",type(userEmail)
		#print "userPass: ",userPass, "Tipo userPass: ",type(userPass)	
		if (len(userPass) >= 7):
			p = hashlib.new('sha1')
			p.update(str(userPass))
			pa = p.hexdigest()
			usuario = Usuario(name=userName, email=userEmail, password=pa)
			usuario.save()
		else:
			raise ValueError('El password debe ser mayor que 7')
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


	
		
