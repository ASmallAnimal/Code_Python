Ls = ['cat','dog',1024]
Lt = Ls
print(Lt)
Ls[1:2]=[1,2,3,4]
print(Ls)
del Ls[::3]
print(Ls)
l1=[]
l1+=[1,2,3,4,5]
l1[1]=6
l1.insert(2,7)
del l1[0]
del l1[1:4]
print(l1)
l1.append(0)
print(l1)
print(0 in l1)
print(0 not in l1)
print(l1.index(0))
print(len(l1))
print(max(l1))
l1.clear()
'''
ls.append(x) add x after the tail
ls.clear()
ls.copy
ls.insert(i,x)
ls.pop(i)
is.remove(x)
'''