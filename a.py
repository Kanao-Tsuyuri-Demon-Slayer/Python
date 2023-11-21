import turtle

def curve(draw):
    draw.pencolor("white")
    draw.pensize(3)
    for i in range(200):
        draw.right(1)
        draw.forward(1)

def draw_heart(draw):
    draw.fillcolor("red")
    draw.begin_fill()
    draw.left(140)
    draw.forward(224)
    curve(draw)
    draw.left(120)
    curve(draw)
    draw.forward(224)
    draw.end_fill()

def draw_decorations(draw):
    draw.penup()
    draw.goto(-80, 300)
    draw.pendown()
    draw.fillcolor("yellow")

    for _ in range(2):
        draw.begin_fill()
        draw.forward(160)
        draw.right(90)
        draw.forward(25)
        draw.right(90)
        draw.forward(160)
        draw.right(90)
        draw.forward(25)
        draw.end_fill()
        draw.right(90)

    draw.penup()
    draw.goto(-550, -20)
    draw.pendown()

    for _ in range(2):
        draw.begin_fill()
        draw.forward(25)
        draw.right(90)
        draw.forward(165)
        draw.right(90)
        draw.forward(115)
        draw.right(90)
        draw.forward(25)
        draw.right(90)
        draw.forward(140)
        draw.right(90)
        draw.forward(190)
        draw.right(90)
        draw.end_fill()
        draw.penup()
        draw.forward(20)
        draw.right(90)
        draw.forward(20)
        draw.pendown()

def main():
    window = turtle.Screen()
    window.bgcolor("black")

    draw = turtle.Turtle()
    draw.speed(5)
    draw.penup()

    draw_heart(draw)

    draw.penup()
    draw.goto(-500, -300)
    draw.pendown()
    draw.hideturtle()

    draw_decorations(draw)

    turtle.done()

if __name__ == "__main__":
    main()
