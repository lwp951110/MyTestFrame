# -*- coding: UTF-8 -*-
import requests,json
from common import logger

# 创建一个http接口类
class HTTP:

    def __init__(self,writer):
        # 创建session对象，模拟浏览器cookie管理
        self.session = requests.session()
        # json解析后结果
        self.jsonres = {}
        # 保存所需要的数据实现关联
        self.params = {}
        self.url = ''
        self.writer = writer

    def seturl(self,url):
        if url.startswith('http'):
            self.url=url
            # print(self.url+'被调用')
            logger.info(self.url+'被调用')
            self.writer.write(self.writer.row,self.writer.clo,'PASS')
            self.writer.write(self.writer.row, self.writer.clo+1, str(self.url))
        else:
            # print('error：非法url地址')
            logger.error('error：非法url地址')
            self.writer.write(self.writer.row,self.writer.clo,'FAIL')
            self.writer.write(self.writer.row, self.writer.clo+1,'error：非法url地址' )

    # 定义post
    def post(self,path,data=None):
        '''
        :param path: url路径
        :param data: 键值对传参
        :return: 无返回值
        '''
        if not path.startswith('http'):
            path= self.url+'/'+path
        try:
            # 判断data是否需要传参数
            result = None
            if data is None or data=='':
                result = self.session.post(path)
            else:
                # 替换参数
                data = self.__getparms(data)
                logger.info(data)
                # 转为字典
                data = self.__todict(data)
                logger.info(data)
                # 发送请求
                result = self.session.post(path,data)
            self.jsonres =json.loads(result.text)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
        except Exception as  e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonres))
            logger.warn(e)

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
           logger.info("PASS")
       else:
           self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
           self.writer.write(self.writer.row, self.writer.clo + 1, res)
           logger.error("FAIL")

    # 添加header
    def addheader(self,key,value):
        value = self.__getparms(value)
        self.session.headers[key] = value
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
        self.writer.write(self.writer.row, self.writer.clo + 1, value)

    # 删除头
    def removeheader(self):
        self.session.headers['token']=None
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
    #
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

    # 获取参数的值
    def __getparms(self,s):
        for key in self.params:
            s = s.replace('{'+key+'}',self.params[key])
        return s

    #转换成字典
    def __todict(self,s):
        # 分割参数个数
        httpparam = {}
        param = s.split('&')
        for ss in param:
            p=ss.split('=')
            httpparam[p[0]] = p[1]

        return httpparam