from turtle import*
import colorsys
bgcolor("black")
pensize(200)
tracer(100)
h=10

for i in range(150):
    c=colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    h+=0.005
    right(120)
    circle(-i*0.5,120)
    circle(-i*0.5,120)
    circle(-i*0.5,120)
    done()