# -*- coding: UTF-8 -*-
import requests,json
from keywords.httpkeys import HTTP
import inspect
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
#
# http = HTTP()
# http.post('http://112.74.191.10:8081/inter/HTTP/auth')
# http.assertequals('status','200')
#
# http.addheader('token','')
# http.post('http://112.74.191.10:8081/inter/HTTP/auth')
# http.assertequals('status','200')
#
# http.addheader('token','a')
# http.post('http://112.74.191.10:8081/inter/HTTP/auth')
# http.assertequals('status','200')
# # token 未授权
# http.addheader('token','')
# http.post('http://112.74.191.10:8081/inter/HTTP/auth')
# http.assertequals('status','200')
#
# http.savejson('t','token')
# http.addheader('token','{t}')
# print(http.session.headers)
# http.post('http://112.74.191.10:8081/inter/HTTP/auth')
# http.assertequals('status','201')
#
# http.post('http://112.74.191.10:8081/inter/HTTP/login','username=Tester&password=123456')
# http.assertequals('status','200')
# http.savejson('id','userid')
# http.post('http://112.74.191.10:8081/inter/HTTP/getUserInfo','id={id}')
# http.assertequals('status','200')
# http.post('http://112.74.191.10:8081/inter/HTTP/logout')
# http.assertequals('status','200')

# a = 'post'
# http = HTTP()
#
# func = getattr(http,a)
# print(func)
# args = inspect.getfullargspec(func).__str__()
# args = args[args.find('args=')+5:args.find(', varargs')]
# args =eval(args)
# args.remove('self')
# print(len(args))
# print(func.__doc__)
# print(args)
#

# a= ['', '', '无token', 'post', 'auth', '', '', '', '']
# http = HTTP()
# func = getattr( http,str(a[3]))
# args = inspect.getfullargspec(func).__str__()
# args = args[args.find('args=')+5:args.find(', varargs')]
# print(args)
# args =eval(args)
# args.remove('self')
# a ={'password': '123456'}
#
# session = requests.session()
# re = session.post(url='http://112.74.191.10:8081/inter/HTTP/auth')
# re1= json.loads(re.text)
# print(re1)
# session.headers['token'] = re1['token']
# result = session.post(url='http://112.74.191.10:8081/inter/HTTP/login',data=a)
#
#

imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
doctor = ImportDoctor(imp)

# 发送webservies
# url为wsdl文档全路径
client1 = Client('http://112.74.191.10:8081/inter/SOAP?wsdl',doctor=doctor)
# 以函数形式
res = client1.service.auth()
res1 = json.loads(res)
print(res)
header = {}
header['token']='a96cc381587b4d698eb364dce9b38089'
client1 = Client('http://112.74.191.10:8081/inter/SOAP?wsdl',doctor=doctor,headers=header)
res = client1.service.login('lwp','123456')
res = client1.service.__getattr__()
print(res)
res = client1.service.logout()
print(res)








