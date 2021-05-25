from excel_config import *
from get_excel import ReadExcel
from main import RunMain
from config.comment import asserts


class open_excel_method:

    def __init__(self, method=None, url=None, headers=None, data=None, payload=None):
        self.tt = title_id()
        self.re = ReadExcel()
        self.method = method
        self.url = url
        self.headers = headers
        self.data = data
        self.payload = payload
        self.run = RunMain()
        self.ass = asserts()

    # def get_lies(self, col, ruo):
    #     self.re.get_call_value(col, ruo)

    def is_run(self):
        rows = self.re.get_hang()
        for i in range(1, rows):
            url = self.re.get_call_value(i, get_url())
            method = self.re.get_call_value(i, get_method())
            headers = eval(self.re.get_call_value(i, get_header()))
            data = eval(self.re.get_call_value(i,get_data()))
            asss = self.re.get_call_value(i, get_asserts())
            # print(type(asss,data,headers))
            if method == 'post':
                res = self.run.run_main(method, url, data=data)
                if self.ass.is_asserts_text(asss, res):
                    self.re.whid_data(i,get_ass_suss(),'pass')
                #     print('断言内容是：%s,断言"{成功}"返回数据包含：%s' % (asss, res))
                else:
                    self.re.whid_data(i, get_ass_suss(), res)
                    # print('断言内容是：%s,断言"{失败}"返回数据包含：%s' % (asss, res))
            else:
                res = self.run.run_main(method, url, headers)
                if self.ass.is_asserts_text(asss, res):
                    self.re.whid_data(i,get_ass_suss(),'pass')
                else:
                    self.re.whid_data(i,get_ass_suss(),res)


if __name__ == '__main__':
    oo = open_excel_method()
    oo.is_run()
