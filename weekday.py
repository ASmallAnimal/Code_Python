dayup = 1.0
dayfactor = 0.01
for i in range (365):
    if i%7 in [6,0]:   #6,7的倍数
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("一年里工作日的力量为{:.2f}".format(dayup))