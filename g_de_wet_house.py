import turtle
from random import randint

p = turtle.Turtle()

screen = turtle.Screen()
screen.setup(width=1300, height=735, startx=0, starty=0)
screen.screensize(1280, 720)
screen.title("Our house, in the middle of the street. by Gustav de Wet, copyright © 2022")
screen.bgcolor("#0083cf")

p.pu()

p.pencolor(0, 0, 0)
draw = 5
tp = 0
p.speed(tp)

def drawCircle(p, r, c):
    p.pd()
    p.speed(draw)
    p.fillcolor(c)
    p.begin_fill()
    p.circle(r)
    p.end_fill()
    p.speed(tp)
    p.pu()

def drawSun(p, c):
    p.pd()
    p.fillcolor(c)
    p.begin_fill()
    for i in range(18):
        p.fd(20)
        p.lt(120)
        p.fd(20)
        p.rt(100)
    p.end_fill()
    p.pu()

def drawCloud(p, r, l, c):
    p.pd()
    p.speed(draw)
    p.fillcolor(c)
    p.begin_fill()
    for i in range(l):
        p.circle(r, 220)
        p.rt(180)
    p.end_fill()
    p.speed(tp)
    p.pu()

def drawRect(p, l, h, c):
    p.pd()
    p.speed(draw)
    p.fillcolor(c)
    p.begin_fill()
    for i in range(2):
        p.fd(l)
        p.lt(90)
        p.fd(h)
        p.lt(90)
    p.end_fill()
    p.speed(tp)
    p.pu()

def drawSquare(p, l, c):
    p.pd()
    p.speed(draw)
    p.fillcolor(c)
    p.begin_fill()
    for i in range(4):
        p.fd(l)
        p.lt(90)
    p.end_fill()
    p.speed(tp)
    p.pu()

def drawFrame():
    p.pd()
    p.speed(draw)
    p.seth(90)
    p.fd(50)
    p.lt(90)
    p.fd(25)
    p.lt(90)
    p.fd(25)
    p.lt(90)
    p.fd(50)
    p.speed(tp)
    p.pu()

def drawRoof(p, c):
    p.pd()
    p.speed(draw)
    p.fillcolor(c)
    p.begin_fill()
    for i in range(2):
        p.lt(60)
        p.fd(220)
    p.lt(150)
    p.fd(380)
    p.end_fill()
    p.speed(tp)
    p.pu()

def drawGrass(f):
    p.pd()
    p.fillcolor("#00c700")
    p.seth(75)
    for i in range(f):
        p.begin_fill()
        grass = randint(5, 20)
        p.fd(grass)
        p.rt(150)
        p.fd(grass)
        p.seth(75)
        p.end_fill()
    p.pu()

def flower():
    p.pd()
    p.color("#008a00")
    p.width(5)
    p.fd(50)
    p.circle(30, 60)
    p.rt(180)
    p.color("black")
    p.width(1)
    drawCloud(p, 5, 9, "#ffff00")
    p.lt(90)
    drawCircle(p, 13.5, "#bfde4e")

def start():
    p.setpos(-690, -360)
    drawRect(p, 1366, 185, "#009600")
    p.seth(90)
    p.fd(185)
    p.seth(0)
    p.fd(75)
    drawGrass(170)

def drawHouse():
    p.seth(0)
    p.setpos(-400, -200)
    drawRect(p, 300, 150, "#804f00")
    p.setpos(-275, -200)
    drawRect(p, 50, 100, "#000000")
    p.setpos(-230, -158)
    drawCircle(p, 4, "gray")
    p.setpos(-365, -135)
    drawSquare(p, 50, "#ffffff")
    p.setpos(-340, -135)
    drawFrame()
    p.setpos(-185, -135)
    drawSquare(p, 50, "#ffffff")
    p.setpos(-160, -135)
    drawFrame()
    p.setpos(-150, -50)
    p.seth(0)
    drawRect(p, 25, 75, "#a63c21")
    p.setpos(-60, -73)
    p.seth(90)
    drawRoof(p, "#ad4800")
    
def theSun():
    p.setpos(360, 175)
    p.seth(310)
    drawSun(p, "#ffb300")
    p.seth(0)
    drawCircle(p, 58, "#ffea00")

def theClouds():
    p.setpos(-250, 170)
    p.seth(15)
    drawCloud(p, 20, 4, "white")
    p.seth(0)
    p.setpos(160, 230)
    drawCloud(p, 15, 4, "white")
    p.seth(10)
    p.setpos(-569, 120)
    drawCloud(p, 10, 4, "white")

def chimney():
    p.seth(0)
    p.setpos(-115, 50)
    drawCloud(p, 3, 9, "#7a7a7a")
    p.setpos(-75, 75)
    drawCloud(p, 6, 9, "#7a7a7a")
    p.setpos(-25, 125)
    drawCloud(p, 9, 9, "#7a7a7a")

def leGrass():
    p.setpos(-500, -275)
    drawGrass(100)
    p.fd(30)
    drawGrass(30)
    p.setpos(260, -290)
    drawGrass(20)
    p.setpos(-580, -225)
    drawGrass(25)

def sunFlower():
    p.seth(90)
    p.setpos(505, -175)
    flower()

def main():
    start()
    drawHouse()
    theSun()
    theClouds()
    chimney()
    leGrass()
    sunFlower()
    p.ht()

main()

window:object = turtle.Screen()
window.exitonclick()