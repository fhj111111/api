from xlutils.copy import copy
import json
import xlrd


class ReadExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../data/case.xlsx'
            self.sheet_id = 0
        self.data = self.open_excel()

    def open_excel(self):
        self.open = xlrd.open_workbook(self.file_name)
        self.data = self.open.sheets()[self.sheet_id]
        return self.data

    # 获取总行数
    def get_hang(self):
        return self.data.nrows

    # 获取总列数
    def get_lie(self):
        return self.data.ncols

    def get_call_value(self, row, col):
        return self.data.cell_value(row, col)


    # 写入内容
    def whid_data(self,col,lou,value):
        workbook = xlrd.open_workbook(self.file_name)  # 打开工作簿
        copy_book = copy(workbook)
        copy_sheet = copy_book.get_sheet(0)
        # 指定单元格写入信息
        copy_sheet.write(col,lou,value)
        # 保存文件
        copy_book.save(self.file_name)






if __name__ == '__main__':
    run = ReadExcel()
    print(run.open_excel())
    print(run.get_lie())
    print(run.get_call_value(9, 5))
