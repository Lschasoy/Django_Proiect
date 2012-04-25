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
	password = 'sdada'
	return password

@step('I create the user')
def create_users(step):
	nombre = 'Marcos'
	mail = 'jose'
	user = Usuario()
	user.create_user(nombre,str(useremail),pas)
	
