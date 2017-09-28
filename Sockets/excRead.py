# 导入xlrd包
import xlrd

class Excel():
    def read_it(self,file_path='d:\\abc.xlsx',index=0):
        data=xlrd.open_workbook(file_path)
        table=data.sheets()[index]
        s=[]
        for i in range(table.nrows):
            for j in range(table.ncols):
                if table.cell(i,j).value!='':
                    s.append(table.cell(i,j).value)
        return s
    def fast_read(self):
        table=self.read_it()
        print(table)

excel=Excel()
excel.fast_read()
