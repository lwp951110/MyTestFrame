# -*- coding: UTF-8 -*-
import requests,json
from keywords.httpkeys import HTTP
import inspect
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
a ={'password': '123456'}

session = requests.session()
re = session.post(url='http://112.74.191.10:8081/inter/HTTP/auth')
re1= json.loads(re.text)
print(re1)
session.headers['token'] = re1['token']
result = session.post(url='http://112.74.191.10:8081/inter/HTTP/login',data=a)


print(result.text)