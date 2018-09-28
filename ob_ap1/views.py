# Create your views here.
#!/usr/bin/python3
# -*- coding:utf-8 -*-
#Name:
#Descripton:
#Author:    smartwy
#Date:
#Version:
from django.shortcuts import render
import pymysql
from django.shortcuts import redirect
from django.contrib import auth
# USER_LIST  = []
# for index in range(20):
# 	temp = {'username':'wangye'+str(index),'email':'abcd@163.com','gender':'M'}
# 	USER_LIST.append(temp)

# USER_LIST = [
# 	{'username': 'root', 'password': '123', 'gender': 'M'},
# 	{'username': '王野', 'password': '456', 'gender': 'M'},
# ]
data = []
db = pymysql.connect('127.0.0.1', 'root', 'password', 'test', port=3306)
cursor = db.cursor()


def home(request):
	return render(request,'home.html')

# def jia(request):
# 	if request.method == 'POST':
# 		temp = {'username': request.POST.get('username'), 'password': request.POST.get('password'),
# 		        'gender': request.POST.get('gender').upper()}
# 		USER_LIST.append(temp)
# 		return render(request,'login.html') # 提交后返回登录页面

class Login_fun(object):
	def login(request):
		if request.method == 'POST':
			usert = request.POST.get('userna')
			pwdt = request.POST.get('passd')
			sql = "select name, passwd from python WHERE name = '%s'" % usert
			cursor.execute(sql)
			data = cursor.fetchone()
			db.commit()
			# print(data)
			if data is not None and usert == data[0] and pwdt == data[1] :
				# return redirect('http://www.baidu.com') # 前端重定向，某个URL
				sql = "select * from host"
				cursor.execute(sql)
				data1 = cursor.fetchall()
				db.commit()
				# print(data1)
				return render(request,'loginok.html',{'userna':usert, 'da': data1})
			else:
				return render(request,'login.html',{'message':'用户名或密码无效！','userna':usert})
		elif request.method == 'GET':
			# sql = "select * from host"
			# cursor.execute(sql)
			# data1 = cursor.fetchall()
			# db.commit()
			# print(data1)
			# return render(request, 'loginok.html', {'da': data1})
			pass
		return render(request,'login.html')
	def edit(request):
		nid = request.GET.get('nid')
		if nid:
			# print('test')
			sql_1 = "DELETE FROM host WHERE id = '%s'" % nid
			sql_2 = 'SELECT * FROM host'
			cursor.execute(sql_1)
			db.commit()
			cursor.execute(sql_2)
			data1 = cursor.fetchall()
			db.commit()
			return render(request,'loginok.html',{'da': data1})
