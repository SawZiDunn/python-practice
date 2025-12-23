import turtle

def draw_square(n):
    for _ in range(4):
        turtle.forward(n)
        turtle.right(90)

def spiral_sq(size):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    while size > 5:
        draw_square(size)
        gap = size * 0.125 # half of the reduced 25%
        size *= 0.75 # 75% of the outer square
        
        turtle.penup()
        turtle.forward(gap)
        turtle.right(90)
        turtle.forward(gap)
        turtle.left(100)
        turtle.pendown()

    turtle.done()

spiral_sq(150)