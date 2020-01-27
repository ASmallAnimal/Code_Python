#试错
#A君365天不休息
#B君休息日休息
def dayUp(df):
    dayup = 1
    for i in range(365):
        if i%7 in [6,0]:   #6,7的倍数
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor+=0.001
print("工作日的努力参数为：{:.3f}".format(dayfactor))