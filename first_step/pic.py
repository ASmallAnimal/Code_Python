import turtle
turtle.setup(650,350,200,200)#窗口的位置
#此时海龟位于画布的中央
turtle.penup()   #画笔提起
turtle.fd(-250)  #海龟位置倒退250px
turtle.pendown()  #画笔落下，开始绘画
turtle.pensize(25) #线条粗25px
turtle.pencolor("purple")   #rgb色彩体系，紫色
turtle.seth(-40)          #角度向下40度
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()

#绝对角度，海龟角度
#seth 方向控制函数，绝对坐标系下的角度
#turtle.left,turtle.right,海龟角度

'''
画笔控制函数
turle.penup->turtle.pu    讲画笔抬起
turtle.pendown->turtle.pd 将画笔放下
turtle.pensize(width)->turtle.with(width)
turtle.pencolor():
颜色的英文小写字符串:turtle.pencolor('purple')
rgb:turtle.pencolor(0.9,0.7,0.3)
rgb的元组值:turtle.pencolor((0.9,0.6,0.3))
'''

'''
运动控制函数
直线
turtle.foeward(d)->turtle.fd(d)
曲线
turtle.circle(r,extent=None) 圆心在上方
r半径
extent弧度
'''

form turtle import* 