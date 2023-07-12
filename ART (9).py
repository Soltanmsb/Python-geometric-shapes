from turtle import*
import colorsys
bgcolor('black')
tracer(10)
pensize(15)
h = 0
for i in range(300):
    c = colorsys.hsv_to_rgb(h,1,1)
    h +=0.005
    pencolor(c)
    fillcolor('black')
    begin_fill()
    for j in range(2):
        fd(i*3)
        rt(60)
        rt(121)
done()