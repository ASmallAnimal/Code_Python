#print
'''
print(a)  打印变量a的值
print('a') 打印a
print(str(a)) 将a转换为字符
'''

'''
a='hello world'
print(len(a))
'''

'''
time是一个包，里面有很多函数
调用包里面的函数
time.sleep
'''
#自定义函数
'''
三个要点：
def 函数名(参数)：
    函数体
    return   #结束函数主体
'''

'''
def greet(name):
    print(name+'你好')
    return
name=input()
greet(name)
'''
'''
def age_1(age):
    if age<15:
        return '儿童'
    elif 15<=age<34:
        return '青年'
    else: return '中年以上'
print(age_1(13))
'''
import random
a=1
while a!=7:
    a=random.randint(1,100)
    print(a)