# -*- coding: UTF-8 -*-
import requests,json

# 创建一个http接口类
class HTTP:

    def __init__(self):
        # 创建session对象，模拟浏览器cookie管理
        self.session = requests.session()
        # json解析后结果
        self.jsonres = {}
        # 保存所需要的数据实现关联
        self.params = {}



    # 定义post
    def post(self,path,data=None):
        # 判断data是否需要传参数
        if data is None:
            result = self.session.post(path)
        else:
            # 替换参数
            data = self.__getparms(data)
            # 转为字典
            data = self.__todict(data)
            # 发送请求
            result = self.session.post(path,data=data)

        self.jsonres =json.loads(result.text)
        print(self.jsonres)

    # 定义断言相等的关键字，用来判断json的key
    def assertequals(self,key,value):
       if str(self.jsonres[key])==str(value):
           print("PASS")
       else:
           print("FAIL")

    # 添加header
    def addheader(self,key,value):
        value = self.__getparms(value)
        self.session.headers[key] = value

    #
    def savejson(self,p,key):
        self.params[p] = self.jsonres[key]
        print(self.params[p])

    # 获取参数的值
    def __getparms(self,s):
        for key in self.params:
            s = s.replace('{'+key+'}',self.params[key])
        return s
    #
    def __todict(self,s):
        # 分割参数个数
        httpparam = {}
        param = s.split('&')
        for ss in param:
            p=ss.split('=')
            httpparam[p[0]] = p[1]

        print(httpparam)
        return httpparam