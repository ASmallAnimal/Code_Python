from random import random
from time import perf_counter
darts=1000*1000
hits = 0.0
start=perf_counter()
for i in range(1,darts+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
pi=4*(hits/darts)
print("pi is {}".format(pi))
print("time is {:.5f}s".format(perf_counter()-start))