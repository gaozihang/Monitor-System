from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.
from . import models
def index(request):
	#get all different ip address in database, for example 192.168.1.1 and 192.168.1.2 ....
	ip = models.Host.objects.values("ip").distinct()
	
	#ip_dict format ip_dict = { ip_addr:[],... }
	ip_dict = {}
	data_json = []
	for i in ip:
		data_list = []
		#get last number data for util, for example, raw = [1, 2, 3, 4, 5] and num = 3, res = [3, 4, 5]
		num = 11
		data = models.Host.objects.filter(ip=i["ip"])[::-1][:num:][::-1]
		for d in data:
			data_list.append(d.util)
		ip_dict[i["ip"]]=data_list
		data_json.append({"name":i["ip"], "data":list(map(float, data_list))})
	ip_dict_json = json.dumps(data_json)
	#print(data_json)
	#print(ip_dict)
	#print(ip_dict_json)
	return render(request, 'index.html', {'ip_dict':ip_dict, 'ip_dict_json':ip_dict_json})

def upload(request):
	if request.POST:
		util = request.POST.get('util')
		mac = request.POST.get('mac')
		ip = request.POST.get('ip')
		print(util, mac, ip)
		host = models.Host()
		host.util = util
		host.mac = mac
		host.ip = ip
	
		host.save()
		return HttpResponse('OK')

	else:
		return HttpResponse('no post data')

def chart(request, ip):
	mac = models.Host.objects.filter(ip=ip)[::-1][0].mac
	return HttpResponse("ip_addr:[" + ip + "], " + "mac_addr:[" + mac + "], "+" OK")

def multi(request):
	ip = models.Host.objects.values("ip").distinct()
	data_list = []
	for i in ip:
		data_list.append(models.Host.objects.filter(ip=i["ip"])[::-1][0].util)
	#print(data_list)
	data_json = json.dumps(data_list)
	print(data_json)
	return HttpResponse(data_json, content_type="application/json")

