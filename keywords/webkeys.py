from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,os

class WEB():
    def __init__(self,writer):
        self.writer = writer
        self.driver = None

    def openbrowser(self,b='cc',d='../lib/chromedriver'):
        try:
            if b=='cc':
                if d =='':
                    d='../lib/chromedriver'
                op = Options()
                op.add_argument('--disable-infobars')
                op.add_argument('--user-data-dir=C:\\Users\\TR\\AppData\\Local\\Google\\Chrome\\User Data')
                self.driver = webdriver.Chrome(executable_path=d, options=op)
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, '打开成功')
        except Exception as e:
            print(e)
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, 'openbrowser调用失败:'+d)


    def openurl(self,url=''):
        if url=='':
            pass
        else:
            try:
                self.driver.get(url)
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, url)
            except Exception as e:
                self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
                self.writer.write(self.writer.row, self.writer.clo + 1, 'openurl调用失败:' +url)

    def click(self,xpath=''):
        if xpath=='':
            pass
        else:
            try:
                ele = self.driver.find_element_by_xpath(xpath=xpath)

                ele.click()
                self.writer.write(self.writer.row, self.writer.clo, 'PASS')
                self.writer.write(self.writer.row, self.writer.clo + 1, xpath)
            except Exception as e:
                print(e)
                self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
                self.writer.write(self.writer.row, self.writer.clo + 1, 'click:' + xpath)

    def inputtext(self,xpath='',keys=''):
        try:
            ele = self.driver.find_element_by_xpath(xpath=xpath)
            ele.send_keys(keys)
            self.writer.write(self.writer.row, self.writer.clo, 'PASS')
            self.writer.write(self.writer.row, self.writer.clo + 1, xpath+'&'+keys)
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, 'FAIL')
            self.writer.write(self.writer.row, self.writer.clo + 1, 'click:' + xpath+'&'+keys)

    def sleep(self,sec=3):
        sec=int(sec)
        time.sleep(sec)
        self.writer.write(self.writer.row, self.writer.clo, 'PASS')
