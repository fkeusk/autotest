import xlwt
import xlrd
from xlutils.copy import copy

def write_line2(path=r'd:\\abc.xlsx',index=0):
    f=xlwt.Workbook()
    f.add_sheet('test2',cell_overwrite_ok='True')
    a=f.get_sheet('test2')
    a.write(0,0,'abc')
    f.save('d:\\abc.xls')
write_line2()


def write_line(path = 'd:\\abc.xlsx', index=0):
    data=xlrd.open_workbook(path)
    sheet1 = data.sheets()[index]
    data2 = copy(data)
    sheet2 = data2.get_sheet(index)
    sheet2.write(1,1,'xxxxxx')
    # sheet2.write(2,2,'xxxxxx')
    # sheet2.write(4,4,'xxxxxx')
    # sheet2.write(5,5,'xxxxxx')
    # data2.save( 'd:\\abc.xls')
    data.save('d:\\abc.xls')
# write_line()


