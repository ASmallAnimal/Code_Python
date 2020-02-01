import turtle as t
t.title('Auto draw')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#get statistics     
detals=[]
f=open("D:/txt/data.txt")
for line in f:
    line=line.replace("\n","")
    detals.append(list(map(eval,line.split(","))))
f.close()
#auto
for i in range(len(detals)):
    t.pencolor(detals[i][3],detals[i][4],detals[i][5])
    t.fd(detals[i][0])
    if detals[i][1]:
        t.right(detals[i][2])
    else:
        t.left(detals[i][2])
t.done()
