def GetNum():
    nums=[]
    iNumstr=input("please input number(ended with enter)")
    while iNumstr!="":
        nums.append(eval(iNumstr))
        iNumstr=input("please input number(ended with enter)")
    return nums

def mean(number):
    s=0.0
    for num in number:
        s+=num
    return s/len(number)

def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev+=(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2+1])
    else:
        med = numbers[size//2] 
    return med

n=GetNum()
m=mean(n)
print("ave:{},variance:{:.2f},med:{}".format(m,dev(n,m),median(n)))
