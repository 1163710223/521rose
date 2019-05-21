import math

import random

import turtle as t

list1 = []

for i in range(5):
    list1.append(int(random.uniform(-500, 500)))

list2 = []

for i in range(5):
    list2.append(int(random.uniform(-200, -50)))

list3 = []

for i in range(8):
    list3.append(int(random.uniform(-400, 400)))

list4 = []

for i in range(8):
    list4.append(int(random.uniform(-150, -50)))

list5 = []

for i in range(7):
    list5.append(int(random.uniform(-300, 300)))

list6 = []

for i in range(7):
    list6.append(int(random.uniform(-200, -100)))

list7 = []

for i in range(18):
    list7.append(int(random.uniform(-500, 500)))

list8 = []

for i in range(18):
    list8.append(int(random.uniform(-100, 100)))

t.speed(0)

# T
t.penup()

t.goto(-330, 250)

t.pendown()

t.color("black")

t.forward(30)

t.backward(15)

t.right(90)

t.forward(45)

# O
t.penup()

t.goto(-290, 220)

t.pendown()

t.circle(15, 180)

t.forward(15)

t.circle(15, 180)

t.forward(15)

# :
t.penup()

t.goto(-240, 240)

t.pendown()

t.fillcolor("black")

t.begin_fill()

t.pencolor("black")

t.circle(3, 360)

t.penup()

t.goto(-240, 210)

t.pendown()

t.circle(3, 360)

t.end_fill()

# L
t.penup()

t.goto(-215, 250)

t.pendown()

t.forward(45)

t.left(90)

t.forward(20)

# I
t.penup()

t.goto(-185, 250)

t.pendown()

t.forward(20)

t.backward(10)

t.right(90)

t.forward(45)

t.right(90)

t.forward(10)

t.backward(20)

# U
t.penup()

t.goto(-155, 250)

t.pendown()

t.left(90)

t.forward(30)

t.circle(15, 180)

t.forward(30)

# B

t.penup()

t.goto(-100, 250)

t.pendown()

t.right(180)

t.forward(45)

t.left(90)

t.forward(10)

t.circle(12, 180)

t.forward(10)

t.right(180)

t.forward(8)

t.circle(10.5, 180)

t.forward(8)

# I
t.penup()

t.goto(-70, 250)

t.pendown()

t.right(180)

t.forward(20)

t.backward(10)

t.right(90)

t.forward(45)

t.right(90)

t.forward(10)

t.backward(20)

# N

t.penup()

t.goto(-40, 205)

t.down()

t.right(90)

t.forward(45)

t.right(150)

t.forward(52.5)

t.left(150)

t.forward(45)

# G

t.penup()

t.goto(30, 250)

t.pendown()

t.left(90)

t.forward(8)

t.circle(22.5, 180)

t.forward(3)

t.circle(12, 90)

t.backward(12)

t.forward(15)

t.left(90)

t.forward(12)

# 将画笔设置到初始化位置
t.penup()

t.goto(0, 0)

t.left(0)

for x, y in list(zip(list1, list2)):
    t.penup()

    t.goto(x, y)

    t.pendown()

    t.fillcolor("#FF6A6A")

    t.begin_fill()

    t.pencolor("#FF6A6A")

    t.forward(40)

    t.circle(20, 180)

    t.right(90)

    t.circle(20, 180)

    t.forward(40)

    t.end_fill()

    t.penup()

    t.goto(x, y)

for x, y in list(zip(list5, list6)):
    t.pendown()

    t.fillcolor("#FFA07A")

    t.begin_fill()

    t.pencolor("#FFA07A")

    t.forward(30)

    t.circle(15, 180)

    t.right(90)

    t.circle(15, 180)

    t.forward(30)

    t.end_fill()

    t.penup()

    t.goto(x, y)

for x, y in list(zip(list3, list4)):
    t.pendown()

    t.fillcolor("#FFD39B")

    t.begin_fill()

    t.pencolor("#FFD39B")

    t.forward(20)

    t.circle(10, 180)

    t.right(90)

    t.circle(10, 180)

    t.forward(20)

    t.end_fill()

    t.penup()

    t.goto(x, y)

for x, y in list(zip(list7, list8)):
    t.pendown()

    t.fillcolor("#FF6A6A")

    t.begin_fill()

    t.pencolor("#FF6A6A")

    t.forward(10)

    t.circle(5, 180)

    t.right(90)

    t.circle(5, 180)

    t.forward(10)

    t.end_fill()

    t.penup()

    t.goto(x, y)


def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)

        t.circle(r, abs(d))


s = 0.2

# t.setup(450*5*s, 750*5*s)

t.pencolor("black")

t.fillcolor("#FF4040")

t.speed(100)

t.penup()

t.goto(0, 750 * s)

t.pendown()

# 绘制花朵形状

t.begin_fill()

t.circle(200 * s, 30)

DegreeCurve(60, 50 * s)

t.circle(200 * s, 30)

DegreeCurve(4, 100 * s)

t.circle(200 * s, 50)

DegreeCurve(50, 50 * s)

t.circle(350 * s, 65)

DegreeCurve(40, 70 * s)

t.circle(150 * s, 50)

DegreeCurve(20, 50 * s, -1)

t.circle(400 * s, 60)

DegreeCurve(18, 50 * s)

t.fd(250 * s)

t.right(150)

t.circle(-500 * s, 12)

t.left(140)

t.circle(550 * s, 110)

t.left(27)

t.circle(650 * s, 100)

t.left(130)

t.circle(-300 * s, 20)

t.right(123)

t.circle(220 * s, 57)

t.end_fill()

# 绘制花枝形状

t.left(120)

t.fd(280 * s)

t.left(115)

t.circle(300 * s, 33)

t.left(180)

t.circle(-300 * s, 33)

DegreeCurve(70, 225 * s, -1)

t.circle(350 * s, 104)

t.left(90)

t.circle(200 * s, 105)

t.circle(-500 * s, 63)

t.penup()

t.goto(170 * s, -190 * s)

t.pendown()

t.left(160)

DegreeCurve(20, 2500 * s)

DegreeCurve(220, 250 * s, -1)

t.fillcolor('#00CD00')

t.penup()

t.goto(670 * s, -180 * s)

t.pendown()

t.right(140)

t.begin_fill()

t.circle(300 * s, 120)

t.left(60)

t.circle(300 * s, 120)

t.end_fill()

t.penup()

t.goto(180 * s, -550 * s)

t.pendown()

t.right(85)

t.circle(600 * s, 40)

t.penup()

t.goto(-150 * s, -1000 * s)

t.pendown()

t.begin_fill()

t.rt(120)

t.circle(300 * s, 115)

t.left(75)

t.circle(300 * s, 100)

t.end_fill()

t.penup()

t.goto(430 * s, -1070 * s)

t.pendown()

t.right(30)

t.circle(-600 * s, 35)

t.done()
