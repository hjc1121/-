#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime
from shixisheng.models import student,Image
from django.template.response import TemplateResponse as TR
def home(request):
	a= {"date":str(datetime.datetime.now())}

	all = student.objects.all()
	a['all'] = all

	all_image = Image.objects.all()
	a['all_img'] = all_image

	return TR(request,"a.html",a)
def hello(request,abcd):
	# return HttpResponse("Hello world ztc" + abcd)
	a={'abcd':"时间","date":str(datetime.datetime.now())}
	all = student.objects.all()
	a['all'] = all
	return TR(request,'my.html',a)
	return render_to_response("my.html",a,context_instance=RequestContext(request))
def world(request,abcd):
	# return HttpResponse("Hello world ztc" + abcd)
	a={'abcd':"时间","date":str(datetime.datetime.now())}
	all = student.objects.all()
	a['all'] = all
	return TR(request,'my.html',a)
	return render_to_response("my.html",a,context_instance=RequestContext(request))
	#添加
def new(request):
	print request.POST
	s = student()
	s.name = request.POST['name']
	s.address = request.POST['address']
	s.content = request.POST['content']
	s.content = 0
	s.save()
	return redirect('/hello/fdsarerq')
	#删除
def delete(request,id):
	s = student.objects.get(id = int(id))
	s = student.objects.get(name="jike")
	s.delete()
	return redirect('/hello/fdsarerq')
	#修改
def edit_view(request,id):
	s = student.objects.get(id = int(id))
	time = datetime.datetime.now()
	d = {"s":s,"t":str(time)}
	return TR(request,'edit.html',d)
	#修改2
def edit(request,id):
	s = student.objects.get(id = int(id))
	s.name = request.POST['name']
	s.address = request.POST['address']
	s.save()
	return redirect('/hello/fdsarerq')