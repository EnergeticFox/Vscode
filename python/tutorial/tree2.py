from turtle import *
import random
import math

def drawTree(length):
    if length>1:
        #隨機角度與長度
        randangle=random.random
        randlength=random.random
        #每次使用函數先繪製線段，再調整角度，這裡是向右的角度轉動
        fd(length)
        right(20*randangle)
        drawTree(length - 10*randlength)

        #這裡是向左的角度轉動
        left(40 * randangle)
        drawTree(length - 10*randlength)

        #為什麼需要再向右轉20度？那是因為我一共向左轉了40度，使用backward後退，必須是相同的角度，不然退回去角度就不同了位置就不會對
        right(20 * randangle)

    up
    backward(length)
    down


setworldcoordinates(-1000,-750,1000,750)
tracer(False)
color('#5E5E5E')
pensize(5)

up
goto(0,-300)#跳到繪製起始點
down

left(80)
fd(140)
drawTree(60)
input
