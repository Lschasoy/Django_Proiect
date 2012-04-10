from lettuce import *
#from lxml import html
#from django.test.client import Client
#from nose.tools import assert_equals
from django.contrib.auth.models import User

@before.all
def set_attr():
    name = ''
    email = ''
    user = User.objects.create_user(name, email, '')

@step('I see the Username (".*")')
def username (step, cadena):
    name = cadena
    user = User.objects.create_user(name, email, '1234')

@step('I see the Email (".*")')
def useremail (step, cadena):
    email = cadena
    user = User.objects.create_user(name, email, '1234')

@step('I check it is correct')
def check_correct(step):
    check_valid(user)  

@step('I create the user')
def create_user(step):
    user.save()
