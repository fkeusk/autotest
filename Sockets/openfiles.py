# # file=open('D:\\openfile.txt','a+')
# # content=file.readlines()
# # file.writelines('\nsomthing,\nanything')
# # file.seek(0)
# # # content2=file.read()
# content=file.read()
# print(content)
# file.close()
# # f=open(r'd:\4.png','wb+')
# # f.write(img)
# # f.close()
# file2=open('d:/wrd/openfile.txt')
# content2=file2.read()
# print(content2)
# file2.close()

import glob, os

s = os.listdir(r'C:\xampp\apache\logs')
g = glob.glob(r'C:\xampp\apache\logs\*.log')
# print(s)
# print(g)
error = []
for i in g:
    xf = open(i,'r')
    c = xf.readlines()
    xf.close()
    for j in c:
        if 'error' in j:
            error.append(j + '\n')
ef = open(r'C:\xampp\apache\logs\newlog2', 'a+')
ef.writelines(error)
ef.seek(0)
con=ef.read()
ef.close()
print (con)

# f.close()
# print (content)
# print(c)
def read_file(name, begin_line, end_line):
    s = []
    f = open(name, 'r')
    con = f.readlines()[begin_line:end_line + 1]
    s.append(con)
    f.close()
    print(s)
    return s


# read_file('d:\\wrd\\openfile.txt',1,4)

def act():
    x = input('输入命令：(WRITE\READ\QUIT)')
    if x == 'write':
        dict = {'aa': 'a', 'bb': 'b'}
        li = ['1', '2', '3']
        f = open(r'd:\wrd\openfile.txt', 'a+')
        f.writelines(dict)
        f.seek(0)
        con = f.read()
        f.close()
        print(con)
    if x == 'read':
        f = open(r'd:\wrd\openfile.txt', 'r')
        con = f.read()
        f.close()
        print(con)
    if x == 'quit':
        print('程序退出')
        quit()

# act()
