import xlrd


class ReadExcel:
    def __init__(self, excel_path, sheet_name):
        #打开excel表格
        self.data = xlrd.open_workbook(excel_path)
        #通过列表名字获取
        self.table = self.data.sheet_by_name(sheet_name)
        #获取第一行key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rownum = self.table.nrows
        #获取总列数
        self.colnum = self.table.ncols

    def dict_data(self):
        #判断总行数不小于1
        if self.rownum <= 1:
            print("总行数小于1")
        else:
            #定义一个空列表来存放表格中的数据
            r = []
            #初始化j，从第二行开始取数据
            j = 1
            #利用循环读取表格中的数据
            for i in range(self.rownum - 1):
                s = {}
                #从第二行取对应的values值
                values = self.table.row_values(j)
                for x in range(self.colnum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

if __name__ == '__main__':
    filepath = "C:/Users/Administrator/Desktop/data.xlsx"
    sheetname = "sheet1"
    data = ReadExcel(filepath, sheetname)
    print(data.dict_data())