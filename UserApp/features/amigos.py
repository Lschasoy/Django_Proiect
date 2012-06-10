from lettuce import *
from Django_Project.UserApp.models import *

@step('I see the Id_user (".*")')
def user (step,id_u):
	id_usu = id_u
	return id_usu

@step('I see the Id_friend (".*")')
def user (step,id_f):
	id_fri = id_f
	return id_fri

@step('I create a friendship')
def friend(step):	
	for k in range(4):
		ami = AmigosFactory.build()
		a = Amigo(id_Usuario = ami.id_Usuario, id_Amigo= ami.id_Amigo)
		a.save()
	
		


