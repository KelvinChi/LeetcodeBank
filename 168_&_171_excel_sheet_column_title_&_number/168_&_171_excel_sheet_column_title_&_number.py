import xlrd
data = xlrd.open_workbook('example.xlsx')
table = data.sheets()[0]
try:
    get = int(input('pls input which row you wanna see'))
    print(table.row_values(get))
except IndexError:
    print('no value in this row')

get = table.nrows
value = input('input which value you wanna search')
for i in range(get):
    if table.row_values(i)[0] == value:
        print('%s is the number you wanna' % i)
    else:
        print('This is no value in this table')

