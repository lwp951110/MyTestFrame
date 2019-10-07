# coding:utf8
import inspect

from common.Excel import Reader, Writer
from keywords.httpkeys import HTTP
from keywords.soapkeys import SOAP
from keywords.webkeys import WEB
from common.excelresult import Res
# 反射获得函数
def getfunc(line,http):
    func = None
    func = getattr(http, str(line[3]))
    return func
# 反射获得参数
def getargs(func):
    if func is None:
        return
    else:
      args = inspect.getfullargspec(func).__str__()
      args = args[args.find('args=') + 5:args.find(', varargs')]
      args = eval(args)
      args.remove('self')
      l = len(args)
      return l
# 运行函数
def run(func,lenargs,line):
    if func is None:
        return

    if lenargs<1:
        func()
        return
    if lenargs<2:
        func(line[4])
        return
    if lenargs<3:
        func(line[4],line[5])
        return
    if lenargs<4:
        func(line[4],line[5],line[6])
        return
    print('errror:目前只支持三个参数的关键字')

# 运行
def runCases():
    reader = Reader()
    writer = Writer()
    res = Res()
    # http = HTTP(writer)
    soap = SOAP(writer)
    # web = WEB(writer)
    reader.open_excel('../lib/cases/SOAP接口用例.xls')
    writer.copy_open('../lib/cases/SOAP接口用例.xls', '../lib/results/result-SOAP接口用例.xls')
    sheetname = reader.get_sheets()
    for sheet in sheetname:
       # 设置当前读写的sheet
       reader.set_sheet(sheet)
       writer.set_sheet(sheet)
       # 默认写第七列
       writer.clo = 7
       for i in range(reader.rows):
          line = reader.readline()
          print(line)
              # 如果第一列或者第二列不为空，不是用例
          if len(line[0])>0 or len(line[1])>0:
              pass
          else:
            writer.row = i
            func = getfunc(line,soap)
            lenargs = getargs(func)
            run(func,lenargs,line)

    writer.save_close()
    res.get_res('../lib/results/result-SOAP接口用例.xls')

runCases()