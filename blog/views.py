from django.shortcuts import render, HttpResponse
from blog.models import Objetos
# Create your views here.
def inicio(resquest):
	arti = Objetos.objects.all()
	return render(resquest,"home.html",{"arti":arti})




	