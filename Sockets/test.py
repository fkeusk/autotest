with open(r'd:\abc.xls','rb+') as f:
    content=f.read()
    print(content)
    f.close()
with open(r'd:\newfile.txt','wb+') as nf:
    nf.write(content)
    nf.close()