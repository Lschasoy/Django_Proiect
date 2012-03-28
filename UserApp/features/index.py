from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_attr():
    @attr = { 'name': 'Example User', 'email': 'user@example.com' }

@step('I see the Username "(.*)"')
def username (step, cadena):
    user = User(@attr.merge('name': cadena))

@step('I see the Email "(.*)"')
def useremail (step, cadena):
    user = User(@attr.merge('email': cadena))
    check_valid(no_email_user)

@step('I check it is correct')
def check_correct(step):
    check_valid(user)  

@step('I create the user')
def create_user(step):
    User.merge!(@attr)



