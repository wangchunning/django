from django.shortcuts import render
from django.shortcuts import *
from apps.user_account.models import *
from django.forms import * 
from django import forms  
from django.http import HttpResponseRedirect
from django.core import validators

class UserAccountForm(ModelForm):  
	class Meta:  
		model = UserAccount
		fields = ['email', 'password', 'gender', 'birthday', 'photo']


class LoginForm(forms.Form):
	email = forms.EmailField(initial='', validators=[validators.MinLengthValidator(10)])
	password = forms.CharField()


def register(req):
	form = UserAccountForm(initial={'birthday': '1980-01-01'})  

	if req.method == 'POST':  
		form = UserAccountForm(req.POST, req.FILES)  
		if form.is_valid():  
			form.save()  
			'''
			如果我们在添加数据到数据库前需要处理一些数据，再入库的话，就可以用到下面一个方法
   			m = form.save(commit=False) save了才能返回model对象
   			m.title = 'sss'
   			m.save()
   			'''
			return HttpResponseRedirect('/login')  

	return render_to_response('register.html', {'form' : form})


def has_login(req):
	return req.session.get('uid', 0) != 0 

def login_user(req):
	_uid = req.session.get('uid')
	return UserAccount.objects.get(uid = _uid)

def login(req):
	form = LoginForm()

	if has_login(req):
		return HttpResponse('you have logged in')

	if req.method == 'POST':

		form = LoginForm(req.POST)
		if not form.is_valid():
			return render_to_response('login.html', {'form': form})

		_user = UserAccount.objects.filter(email__exact = form.cleaned_data['email'])
		print _user
		if _user and _user[0].password == form.cleaned_data['password']:
			req.session['uid'] = _user[0].uid
			return HttpResponse('logged in')
		else:
			return render_to_response('login.html', {'err': 'login failed'})


	if req.method == 'GET':
		return render_to_response('login.html', {'form': form})

def logout(req):
	del req.session['uid'];
	return render_to_response('login.html')



def index(req):
	if not has_login(req):
		# raise Http404('Only POSTs are allowed')
		return HttpResponseRedirect('/login/')

	_user = login_user(req)
	return render_to_response('index.html', {'user' : _user})


