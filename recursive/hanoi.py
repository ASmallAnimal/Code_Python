count=0
def hanoi(A,B,C,n):
    global count
    if n==1:
        print("{}:{}-->{}".format(1,A,C))
        count+=1
    else:
        hanoi(A,C,B,n-1)
        print("{}:{}-->{}".format(n,A,C))
        count+=1
        hanoi(B,A,C,n-1)
n=int(input())
hanoi('A','B','C',n)
print(count)