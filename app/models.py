# -*- coding: utf-8 -*-
__author__ = 'ma'

from django.db import models
import paramiko, logging ,dwebsocket, time


class Server(models.Model):
	hostname = models.CharField(max_length=50, verbose_name=u"hostname", unique=True)
	ip = models.GenericIPAddressField(u"server ip", max_length=15)
	port = models.IntegerField(u'ssh port')
	username = models.CharField(max_length=50, verbose_name=u"ssh username", default='', blank=True)
	password = models.CharField(max_length=50, verbose_name=u"ssh password", default='', blank=True)
	description = models.CharField(max_length=128, verbose_name=u"description", default='', blank=True)

	def __str__(self):
		return self.hostname

	# 获取paramiko的channel.exec_command对象
	def get_channel_over_ssh(self):
		try:
			ssh_client = paramiko.SSHClient()
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client.connect(self.ip, self.port, self.username, self.password)
			channel = ssh_client.invoke_shell(term='xterm')
			channel.settimeout(0)
			return (channel)
		except Exception as e:
			logging.error(e)
			return None 

	# 发送shell的输出结果到web页面
	def shell_output_sender(self, request, channel):
		while True:
			if request.websocket.is_closed(): # 检测客户端心跳，如果客户端关闭，则停止读取和发送日志
				print ('websocket is closed')
				channel.close()
				break
			if channel.recv_ready():
				recvfromssh = channel.recv(16371)
				request.websocket.send(recvfromssh)
			time.sleep(0.1)

	# 接受页面输入并发送到shell
	def shell_input_reciever(self,request, channel):
		while True:
			if request.websocket.is_closed(): # 检测客户端心跳，如果客户端关闭，则停止读取和发送日志
				print ('websocket is closed')
				channel.close()
				break
			for msg in request.websocket:
				cmd = msg.decode()
				channel.send(cmd)

# 用户
class User_Info(models.Model):
	username = models.CharField("用户名", max_length=128, blank=False, unique=True)
	password = models.CharField("密码", max_length=128, blank=False)
	email = models.CharField("邮箱", max_length=128, blank=True)
	is_superuser = models.BooleanField("是否超级用户", blank=False)
	description = models.CharField("描述", max_length=128, blank=True)

	def __str__(self):
		return self.username