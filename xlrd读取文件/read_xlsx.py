import xlrd
import json
workbook = xlrd.open_workbook('C:/Users/Administrator/Desktop/data.xlsx')

worksheet = workbook.sheet_by_name('测试用例')
'''获取第二行数据，xlsx表格里面的数据是列表形式的'''
# print(worksheet.row_values(1))
# print(worksheet.col_values(0))
# print(worksheet.cell_value(1, 0))
'''读取的是列表形式的数据，无法使用'''
# list = []
# for i in range(worksheet.nrows):
#     list.append(worksheet.row_values(i))
# print(list)

def get_data():
    sheetdata=[]
    headers = worksheet.row_values(0)
    for r in range(1, worksheet.nrows):#或者worksheet.nrows-1
        row_vars = worksheet.row_values(r)
        tmp_dict = {}
        # tmp_dict[headers[0]] = row_vars[0]
        # tmp_dict[headers[1]] = row_vars[1]
        # tmp_dict[headers[2]] = row_vars[2]
        # tmp_dict[headers[3]] = row_vars[3]
        # for i in range(len(headers)):
        #     tmp_dict[headers[i]] = row_vars[i]
        tmp_dict = dict(zip(headers, row_vars))
        sheetdata.append(tmp_dict)
    return sheetdata

print(get_data())






