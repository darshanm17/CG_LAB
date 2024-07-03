import turtle
def b(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    xs=1 if x1<x2 else -1
    ys=1 if y1<y2 else -1
    error=2 * dy - dx
    linepoints=[]
    x,y=x1,y1
    for _ in range(dx + 1):
        linepoints.append((x,y))
        if error>0:
            y+=ys
            error-=2 * dx
        error+=2 * dy
        x+=xs
    return linepoints
turtle.setup(500,500)
turtle.speed(0)
x1,y1=100,100
x2,y2=400,300

linepoints=b(x1,y1,x2,y2)
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
for x,y in linepoints:
    turtle.goto(x,y)
turtle.exitonclick()
