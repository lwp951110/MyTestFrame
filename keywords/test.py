# -*- coding: UTF-8 -*-
import requests,json
from keywords.httpkeys import HTTP


http = HTTP()
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status','200')

http.addheader('token','')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status','200')

http.addheader('token','a')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status','200')
# token 未授权
http.addheader('token','')
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status','200')

http.savejson('t','token')
http.addheader('token','{t}')
print(http.session.headers)
http.post('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status','201')

http.post('http://112.74.191.10:8081/inter/HTTP/login','username=Tester&password=123456')
http.assertequals('status','200')
http.savejson('id','userid')
http.post('http://112.74.191.10:8081/inter/HTTP/getUserInfo','id={id}')
http.assertequals('status','200')
http.post('http://112.74.191.10:8081/inter/HTTP/logout')
http.assertequals('status','200')