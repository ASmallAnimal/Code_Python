A='123py'
A=set(A)
for a in A:
    print(a,end="")
try:
    while True:
        print(A.pop(),end="")
except:
    pass

# when A is empty, exe will have a error captured by trt/except
