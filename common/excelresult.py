# coding:utf8
from common.Excel import Reader
from common import logger

class Res:
    '''
    统计用例的结果
    '''
    def __init__(self):
        self.sumarry = {}
    def get_res(self,result_path):
        self.sumarry.clear()
        status = 'Fail'
        # 标志是否有
        flag = True
        # 总用例数
        totalcount = 0
        # 总通过数
        totalpass = 0

        reader =  Reader()
        reader.open_excel(result_path)
        for n in reader.get_sheets():
            reader.set_sheet(n)
            row = reader.rows
            reader.r = 1

        for i in range(1,row):
            line = reader.readline()
            logger.info(line)

            if not (line[0]==''and line[1]==''):
                pass
            else:
                if len(line) < 7 or line[7] =='':
                    flag = False
                    print('1'+str(flag))
                else:
                    totalcount = totalcount + 1
                    if line[7] == 'PASS':
                        totalpass +=1
                    else:
                        flag = False
                        print('2'+str(flag))

        if flag:
            status = 'PASS'
        try:
            p = int(totalpass * 10000 / totalcount)
            passrate = p / 100
        except Exception as e:
            passrate = 0.0
            logger.exception(e)
        self.sumarry['casecount'] = str(totalcount)
        self.sumarry['passrate'] = str(passrate)
        self.sumarry['status'] = status
        return self.sumarry
if __name__ == '__main__':
    res =Res()
    r = res.get_res('../lib/results/result-WEB接口用例.xls')
    print(r)












