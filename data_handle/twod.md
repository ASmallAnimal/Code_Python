# write & read

## write

fo=open(fname)  
ls=[]  
for line in fo:  
    \t line  
    \t la.append(line.split(","))
fo.close()  

## read

ls=[[],[],[]]
f=open(fname,"w")  
for item in ls:  
    \t f.write(','.join(item)+'\n')  
f.close()
