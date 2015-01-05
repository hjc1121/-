#coding:utf-8
from django.db import cj

class student(cj.Model):
	name = cj.CharField(max_length=30)
	zf = cj.CharField(max_length=50)
	