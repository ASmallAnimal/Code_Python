#<f>.write(s)
#<f>.writelines(lines(list))
# ls=["z","a","f"]
# f.writelines(ls)-->'zaf'
#<f>.seek<offset>-->offset:0 <head>,1 <currency>,2 <end>
fo = open("D:/txt/output.txt","w+")
ls=["China","America","France"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()