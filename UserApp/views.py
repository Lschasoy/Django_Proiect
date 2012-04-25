# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render_to_response
from Django_Project.UserApp.models import *

def users_list(request):
	user_list = Usuario.objects.all()
	return render_to_response ('users_list.html',{'lista_usuarios': user_list});


def users_search(request,id_user):
	user_list = Usuario.objects.get(id = id_user)
	return render_to_response ('users_search.html',{'usuario': user_list, 'id_user': id_user});
