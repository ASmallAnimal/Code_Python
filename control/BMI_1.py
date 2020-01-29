height, weight = eval(input("please input height(metre) and weight(kg) divided with ',' :"))
bmi = weight / pow(height,2)
print("BMI number is {:.2f}".format(bmi))
who, nat="",""
if bmi< 18.5:
    who, nat ="thin","thin"
elif 18.5<=bmi<24:
    who, nat="normal","normal"
elif 24<=bmi<24:
    who, nat="nomal","fat"
elif 25<=bmi<28:
    who,nat="fat","fat"
elif 28<=bmi<30:
    who,nat="fat","too fat"
else:
    who,nat="too fat","too fat"
print("who:"+who,"nat:"+nat)