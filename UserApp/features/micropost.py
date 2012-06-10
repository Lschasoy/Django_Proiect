from lettuce import *
from Django_Project.UserApp.models import *

@step('I see the Id_user (".*")')
def user (step,id_u):
	id_usu = id_u
	return id_usu

@step('I see the Text (".*")')
def micro (step, texto):
	text= texto
	return text
@step('And I test the text does not exceed 140 character (".*")')
def text_size(step,texto):
	if (len(texto) <= 140):
		return True
	else:
		return False

@step('I create the post')
def crear_micro (step):
	for i in range(10):
		micro_ = MicropostFactory.build()
		print "Micropost: ", micro_.texto
		micro_1 = Micropost()
		for j in range(1,5):
			micro_1.create_post(j, micro_.texto)

