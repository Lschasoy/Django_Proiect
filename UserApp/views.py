from django.http import HttpResponse, HttpRequest
from django.template import loader, Context
from django.shortcuts import render_to_response
from Django_Project.UserApp.models import *

def users_list(request):
	if request.session['id_usuario']:
		siguiendo = Amigo.objects.filter(id_Usuario=request.session['id_usuario'])
		no_siguiendo=Usuario.objects.all()
		user_id = request.session['id_usuario']
		print "Todos", user_id
		
		siguiendo_amigo = Amigo.objects.raw("Select * from UserApp_Usuario where id not in (Select id_Amigo_id from UserApp_Amigo where (id_Usuario_id = %s))",[user_id])
		cont =0
		seguir=[]
		for lista in siguiendo_amigo:
			if not (siguiendo_amigo[cont].id == request.session['id_usuario']):
				seguir.append(siguiendo_amigo[cont])
			cont +=1
		print "no_siguiendo", seguir
		print "tipo: ", type(siguiendo_amigo)
		return render_to_response ('users_list.html',{'lista_usuarios': seguir});
	return HttpResponse('sesion no iniciada')

def users_search(request,id_user):
	user_list = Usuario.objects.get(id = id_user)
	micro_list = Micropost.objects.filter (resumen=user_list.id)
	return render_to_response ('users_search.html',{'usuario': user_list, 'id_user': id_user, 'micropost': micro_list});

def users_edit(request,id_user):
	if (request.method == 'POST'):
		user_form=UserForm(request.post, instance=request.user)
		if user_form.is_valid():
			user_form.save()
			print "Formulario guardado"
	else:
		user_form=UserForm(instance=request.user)
		print "Generando formulario"
	return render_to_response ('users_edit.html',{'user_form': user_form});

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		user_name = Usuario.objects.filter(name=q)
		if user_name:
			user_nam = Usuario.objects.get(name=q)
			print "user_name: ",user_name
			return render_to_response('search_result.html', {'usuario': user_nam, 'query': q})
		else:
			return render_to_response('search_result.html', {'usuario': user_name, 'query': q})
	else:
		return render_to_response('search_form.html', {'error': True})
		
def creacion(request):
	return render_to_response('form_v2.html')
	
def create_u(request):
	
	if 'qname' in request.POST and request.POST['qname']:
		qname1 = request.POST['qname']
		qemail1 = request.POST['qemail']
		qpass1 = request.POST['qpass']
		qcpass1 = request.POST['qcpass']
		qimg = request.POST['qimg']
		u = Usuario()
		u.create(qname1,qemail1,qpass1,qcpass1,qimg)
		user_tl = Usuario.objects.get(name = qname1)
		return render_to_response('Tl_v2.html',{'user_tl': user_tl})

	else:
		return HttpResponse('error')

def login(request):
	request.session.set_test_cookie()
	return render_to_response('login_v2.html')

def login_u(request):
	if 'qname' in request.POST and request.POST['qname']:
		qname1 = request.POST['qname']
		qpass1 = request.POST['qpass']
		u = Usuario()
		if u.authenticate(qname1,qpass1):
			m = Usuario.objects.get(name=request.POST['qname'])
			request.session['id_usuario'] = m.id
			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()
				html = "<html><head> <meta http-equiv=\"refresh\" content=\"0;url=/session/\">  </head><body>   </body></html>"
				return HttpResponse(html)
			else:
				return HttpResponse('Habilite las cokkies')
		else:
			return render_to_response('login_v2.html',{'error': True})
	else:
		return HttpResponse('error')

def session(request):
	if request.session['id_usuario']:
		user_tl = Usuario.objects.get(id = request.session['id_usuario'])
		micro_list = Micropost.objects.filter (resumen=request.session['id_usuario'])
		a={}
		if Amigo.objects.filter(id_Usuario=user_tl.id):
			siguiendo = Amigo.objects.filter(id_Usuario=user_tl.id)
			seguidores = Amigo.objects.filter(id_Amigo=user_tl.id)
			
			for it in range(len(siguiendo)):
				amigo_list =(Usuario.objects.get (name=siguiendo[it].id_Amigo))
				micro_list_amigo=(Micropost.objects.filter (resumen=amigo_list))
				for item in range(len(micro_list_amigo)):
					a[micro_list_amigo[item].create_at] = [micro_list_amigo[item],amigo_list]
		else:
			siguiendo = Amigo.objects.filter(id_Usuario=user_tl.id)
			seguidores = Amigo.objects.filter(id_Amigo=user_tl.id)
					
		for item in range(len(micro_list)):
			a[micro_list[item].create_at] = [micro_list[item],user_tl]
								
		micro_sort=a.items()
		micro_sort.sort(key = lambda a:a[0], reverse=True)
				
		return render_to_response('Tl_v2.html',{'user_tl': user_tl, 'post_amigos': micro_sort, 'count_sig':siguiendo.count(),'count_seg':seguidores.count()})
			
	return HttpResponse('sesion no iniciada')

def crear_post(request):
	if request.session['id_usuario']:
		user_tl = Usuario.objects.get(id = request.session['id_usuario'])
		if 'qtext' in request.POST and request.POST['qtext']:
			qtext = request.POST['qtext']
			micro = Micropost()
			micro.create_post(request.session['id_usuario'],qtext)
			html = "<html><head> <meta http-equiv=\"refresh\" content=\"0;url=/session/\">  </head><body>   </body></html>"
			return HttpResponse(html)
	return HttpResponse('sesion no iniciada')


def logout(request):
	try:
		del request.session['id_usuario']
	except KeyError:
		pass
	html = "<html><head> <meta http-equiv=\"refresh\" content=\"0;url=/login/\">  </head><body>   </body></html>"
	return HttpResponse(html)

def siguiendo(request):
	if request.session['id_usuario']:
		siguiendo = Amigo.objects.filter(id_Usuario=request.session['id_usuario'])
		siguiendo_amigo = []
		for it in range(len(siguiendo)):
			siguiendo_amigo.append (Usuario.objects.get(name = siguiendo[it].id_Amigo))
		return render_to_response ('siguiendo.html',{'lista_usuarios': siguiendo_amigo})
	return HttpResponse('sesion no iniciada')


def seguido(request):
	if request.session['id_usuario']:
		seguidores = Amigo.objects.filter(id_Amigo=request.session['id_usuario'])
		seguidores_amigo = []
		for it in range(len(seguidores)):
			seguidores_amigo.append (Usuario.objects.get(name = seguidores[it].id_Usuario))
		return render_to_response ('seguido.html',{'lista_usuarios': seguidores_amigo})
	return HttpResponse('sesion no iniciada')


def borrar_siguiendo (request):
	qid = request.POST['qid']
	siguiendo = Amigo.objects.get(id_Usuario=request.session['id_usuario'],id_Amigo=qid)
	siguiendo.delete()
	html = "<html><head> <meta http-equiv=\"refresh\" content=\"0;url=/siguiendo/\">  </head><body>   </body></html>"
	return HttpResponse(html)

def borrar_seguido (request):
	qid = request.POST['qid']
	siguiendo = Amigo.objects.get(id_Amigo=request.session['id_usuario'],id_Usuario=qid)
	siguiendo.delete()
	html = "<html><head> <meta http-equiv=\"refresh\" content=\"0;url=/seguido/\">  </head><body>   </body></html>"
	return HttpResponse(html)

def seguir (request):
	qid = request.POST['qid']
	user = Usuario.objects.get(id=request.session['id_usuario'])
	amigo = Usuario.objects.get(id=qid)
	seguir = Amigo (id_Usuario=user,id_Amigo=amigo)
	seguir.save()
	html = "<html><head> <meta http-equiv=\"refresh\" content=\"0;url=/users/\">  </head><body>   </body></html>"
	return HttpResponse(html)

def solo (request,id_user): 
	if request.session['id_usuario']:
		amigo = Amigo.objects.filter(id_Usuario=request.session['id_usuario'],id_Amigo=id_user)
			
		if ((int(id_user)==int(request.session['id_usuario'])) or (amigo)):
			user_tl = Usuario.objects.get(id = id_user)
			micro_list = Micropost.objects.filter (resumen=id_user)
			a={}

			siguiendo = Amigo.objects.filter(id_Usuario=user_tl.id)
			seguidores = Amigo.objects.filter(id_Amigo=user_tl.id)
						
			for item in range(len(micro_list)):
				a[micro_list[item].create_at] = [micro_list[item],user_tl]
									
			micro_sort=a.items()
			micro_sort.sort(key = lambda a:a[0], reverse=True)
					
			return render_to_response('Tl_user.html',{'user_tl': user_tl, 'post_amigos': micro_sort, 'count_sig':siguiendo.count(),'count_seg':seguidores.count()})
		else:
			html = "<html><head> <meta http-equiv=\"refresh\" content=\"0;url=/Session/\">  </head><body>   </body></html>"
			return HttpResponse(html)
	return HttpResponse('sesion no iniciada')

def perfil (request):
	if request.session['id_usuario']:
		user = Usuario.objects.get(id=request.session['id_usuario'])
	return render_to_response('form_mod.html',{'usuario':user})


def modificar(request):
	if request.session['id_usuario']:
		qname1 = request.POST['qname']
		qemail1 = request.POST['qemail']
		qpass1 = request.POST['qpass']
		qcpass1 = request.POST['qcpass']
		qimg = request.POST['qimg']
		user = Usuario.objects.get(id=request.session['id_usuario'])
		if qpass1:
			if ((user.long_p(qpass1)==True) & (user.short_p(qpass1)==True) & (user.confirm_p(qpass1,qcpass1) == True)):
				user.name= qname1
				user.email = qemail1
				user.gravatar_img = qimg
				p = hashlib.new('sha1')
				p.update(str(qpass1))
				pa = p.hexdigest()
				user.password = pa
				user.save()
				return HttpResponse('listo')
			else:
				return HttpResponse('no listo')
		else:
			user.name= qname1
			user.email = qemail1
			user.gravatar_img = qimg
			user.save()
			return HttpResponse('listo')
		
