# -*- coding: utf-8 -*-
__author__ = 'ma'

import time, os, logging, paramiko, multiprocessing, threading, re
from django.shortcuts import render, redirect


# 定义登陆状态控制器装饰器函数，如果未登录，则跳转到登录页面
def auth_controller(func):
	def wrapper(request,*args,**kwargs):
		if not request.session.get("islogin"):
			return redirect("/login/")
		return  func(request,*args, **kwargs)
	return wrapper