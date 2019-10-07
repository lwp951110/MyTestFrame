# -*- coding: UTF-8 -*-
import requests,json

from common.Excel import Writer
from keywords.httpkeys import HTTP
import inspect
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
from keywords.soapkeys import SOAP

# soap= SOAP()
# soap.adddoctor('')
# soap.setwsdl('http://112.74.191.10:8081/inter/SOAP?wsdl')
# soap.callmethod('auth','')
# soap.savejson('token','token')
# soap.addheader('token','{token}')
# soap.callmethod('logout','')
# soap.assertequals("status",200)
#
#
#
# res = requests.session()
# result = res.get('https://ke.qq.com/course/list/%E7%89%B9%E6%96%AF%E6%B1%80%E5%AD%A6%E9%99%A2?tuin=3ec2bac8')
# print(result)

from keywords.webkeys import WEB
writer = Writer()
web=WEB(writer)
web.openbrowser(b='cc',d='')
web.openurl('http://112.74.191.10:8000/Home/user/login.html')
web.sleep(3)
web.inputtext('//*[@id="username"]','13800138006',)
web.inputtext('//*[@id="password"]','123456')
web.inputtext('//*[@id="verify_code"]','111')
web.click('//*[@id="loginform"]/div/div[6]/a')
web.click('/html/body/div[1]/div/div/div/div[2]/a[2]')