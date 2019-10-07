import requests,json
import inspect
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
from common import logger

class SOAP:
    def __init__(self,writer):
        self.wsdl= ''
        self.doctor= None
        self.wsdl_url = ''
        self.client = None
        self.params = {}
        self.header = {}
        self.result = ''
        self.jsonres = None
        self.actualresult = ''
        self.writer = writer


    def adddoctor(self,targetNamespace,XMLSchema='',location=''):
        if  XMLSchema=='':
            XMLSchema='http://www.w3.org/2001/XMLSchema'
        if  location == '':
            location= 'http://www.w3.org/2001/XMLSchema.xsd'

        imp = Import(XMLSchema, location=location)
        imp.filter.add(targetNamespace)
        self.doctor = ImportDoctor(imp)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.doctor))

    def setwsdl(self,url):
        if not url.startswith('http'):
            logger.error('FIAL')
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, url)
        else:
            self.wsdl_url=url
            self.client= Client(url,doctor=self.doctor,headers=self.header)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, self.wsdl_url)


    def addheader(self,key,value):
         value=self.__getparms(value)
         self.header[key] = value
         self.client = Client(self.wsdl_url,doctor=self.doctor,headers=self.header)
         self.writer.write(self.writer.row, self.writer.clo, 'PASS')
         self.writer.write(self.writer.row, self.writer.clo + 1, self.header[key] )



    def callmethod(self,meth,parm):
        try:
            if not parm=='':
                p = parm.split('、')
            if parm=='':
                self.result = self.client.service.__getattr__(meth)()
            else:
                self.result = self.client.service.__getattr__(meth)(*p)

            self.jsonres =json.loads(self.result)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, meth)
            print(self.jsonres)
        except Exception as e:
            print(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, meth+'调用失败')


    # 定义断言相等的关键字，用来判断json的key
    def assertequals(self,key,value):
       res=''
       try:
           res = str(self.jsonres[key])
       except Exception as e:
           logger.warn(e)

       if res==str(value):
           self.writer.write(self.writer.row, self.writer.clo, 'PASS')
           self.writer.write(self.writer.row, self.writer.clo + 1, res)
           print("PASS")

           logger.info("PASS")
       else:
           self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
           self.writer.write(self.writer.row, self.writer.clo + 1, res)
           print("FAIL")
           logger.error("FAIL")

    def savejson(self,p,key):
        res=''
        try:
            res=self.jsonres[key]
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            logger.warn(e)
        self.params[p] = res
        logger.info(self.params[p])
        self.writer.write(self.writer.row, self.writer.clo+1, str(self.params))

    def __getparms(self,s):
        for key in self.params:
            s = s.replace('{'+key+'}',self.params[key])
        return s


