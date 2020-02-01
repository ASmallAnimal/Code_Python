fo= open(D:/txt/txt1.txt)
txt=fo.read(2) #2 bits
while txt != "":
    txt=fo.read(2)
fo.close()
