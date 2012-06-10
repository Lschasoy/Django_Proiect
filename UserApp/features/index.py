from lettuce import *
from Django_Project.UserApp.models import *



@step('I see the Username (".*")')
def username (step, cadena):
	name = cadena
	name = 'Marcos'
	return name

#======================================
@step('I see the Email (".*")')
def useremail (step, cadena):
	emai = ' ' 
	email = str(cadena)
	return str(email)

#======================================
@step('I see the Password (".*")')
def userpass (step, cadena):
	password = cadena
	return password
#======================================
@step('I see the Password confirmation (".*")')
def confirmar_pass (step, cadena):
	passw = cadena
	user = Usuario()
	user.confirm_p(passw,passw)

@step('I reject the short password (".*")')
def short_pass(step, cadena):
	passw = cadena
	user = Usuario()
	user.short_p(passw)

@step('I reject the long password (".*")')
def long_pass(step, cadena):
	passw = cadena
	user = Usuario()
	user.long_p(passw)

# nos falta validar todos los campos
@step('I create the user')
def create_users (step):
	for i in range(10):
		user = UserFactory.build()
		print "user.name= ", user.name
		print "user.email= ", user.email
		print "user.password = ", user.password
		user_ = Usuario()
		user_.create(user.name, user.email, user.password,user.password,"")


