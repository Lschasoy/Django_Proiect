from lettuce import *
from Django_Project.UserApp.models import *

@before.all
def set_attr():
	name = ''
	email = ''
	password = ''
#======================================
@step('I see the Username (".*")')
def name (step, cadena):
    name = cadena

def username(self):
	return self.__name  

#======================================
@step('I see the Email (".*")')
def useremail (step, cadena):
    email = cadena

def email(self):
	return self.__email

#======================================
@step('I see the Password (".*")')
def userpass (step, cadena):
    password = cadena

def password(self):
	return self.__password


@step('I create the user')
def create_users(step):
	UserManager.create_user(name, email, password)
