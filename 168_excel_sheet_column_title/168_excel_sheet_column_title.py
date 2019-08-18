import xlrd
data = xlrd.open_workbook('example.xlsx')
table = data.sheets()[0]
try:
    get = int(input('pls input which row you wanna see'))
    print(table.row_values(get))
except IndexError:
    print('no value in this row')

