from lettuce import *
<<<<<<< HEAD
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
=======
#from lxml import html
#from django.test.client import Client
#from nose.tools import assert_equals
from django.contrib.auth.models import User

@before.all
def set_attr():
    name = ''
    email = ''
    password = ''
    user = User.objects.create_user(name, email, password)

@step('I see the Username (".*")')
def username (step, cadena):
    name = cadena
    user = User.objects.create_user(name, email, password)

@step('I see the Email (".*")')
def useremail (step, cadena):
    email = cadena
    user = User.objects.create_user(name, email, password)

@step('I check it is correct')
def check_correct(step):
    check_valid(user)  

@step('I create the user')
def create_user(step):
    user.save()
>>>>>>> b86d82516e5840ff9ecea170c1bc1eda110c2583
