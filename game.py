import time
import turtle

ekran = turtle.Screen()
ekran.bgcolor("lightblue")
ekran.title("physics")
ekran.tracer(0)
ekran.setup(width=1000, height=800)

FPS = 60
LEVEL = 4
COSTUME = 1


glava = turtle.Turtle()
glava.shape("circle")
glava.shapesize(2)
glava.color ("red")
glava.penup()
glava.goto(-280 , 0)
glava.yvelocity = 0
glava.xvelocity = 0
glava.gravity = 0.05
glava.radius = 10 * glava.shapesize()[0]
glava.bounce = -0.9

level_pen = turtle.Turtle()
level_pen.hideturtle()
level_pen.speed(0)
level_pen.penup()

def draw_square(corner1, corner2, corner3, corner4, color):
    level_pen.fillcolor(color)

    level_pen.penup()
    level_pen.goto(corner1)
    level_pen.pendown()

    level_pen.begin_fill()
    level_pen.goto(corner2)
    level_pen.goto(corner3)
    level_pen.goto(corner4)
    level_pen.goto(corner1)

    level_pen.end_fill()


def draw_circle(center, radius, color):
    level_pen.fillcolor(color)
    level_pen.penup()
    level_pen.goto(center[0], center[1] - radius)
    level_pen.pendown()

    level_pen.begin_fill()
    level_pen.circle(radius)
    level_pen.end_fill()

def move(speed):
    if speed < 10 and speed > -10:
        glava.xvelocity += speed

def draw_level(level, costume):
    level_pen.clear()
    glava.shape("circle")
    glava.shapesize(2)
    glava.color ("red")
    glava.penup()
    if costume == 1:
        glava.goto(-280 , 0)
        glava.yvelocity = 0
        glava.xvelocity = 0
    glava.gravity = 0.05
    glava.radius = 10 * glava.shapesize()[0]
    glava.bounce = -0.9
    if level == 1:
        draw_square((-400, -150), (50, -150), (50, -200), (-200, -200), "grey")
        draw_circle((275, -175), 25, "gold")
    if level == 2:
        if costume == 1:
            draw_square((-400, -150), (-100, -150), (-100, -200), (-200, -200), "grey")
            draw_square((200, -150), (400, -150), (400, -200), (200, -200), "grey")
        if costume == 2:
            glava.setx(-500)
            draw_square((-400, -150), (200, -150), (200, -200), (-400, -200), "grey")
            draw_circle((275, -175), 25, "gold")
    if level == 3:
        draw_square((-400, -150), (-100, -150), (-100, -200), (-400, -200), "grey")
        draw_square((200, -150), (400, -150), (400, -200), (200, -200), "yellow")
        draw_square((-300, 300), (100, 300), (100, 250), (-300, 250), "grey")
        draw_circle((-375, 275), 25, "gold")
    if level == 4:
        if costume == 1:
            draw_square((-400, -150), (-100, -150), (-100, -200), (-400, -200), "grey")
            draw_square((100, -150), (300, -150), (300, -200), (100, -200), "yellow")
            draw_square((0, 300), (510, 300), (510, 250), (0, 250), "grey")
            draw_square((450, 250), (500, 250), (500, -400), (450, -400), "grey")
            draw_circle((375, 350), 25, "gold")



def colision(level, costume):
    global LEVEL, COSTUME
    if glava.ycor() <= -400:
        COSTUME = 1
        draw_level(LEVEL, COSTUME)
    if level == 1:
        if glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200 and glava.xcor() - glava.radius < 50:
            glava.yvelocity = glava.yvelocity * glava.bounce
        if glava.xcor() - glava.radius <= -400:
            glava.xvelocity = glava.xvelocity * -0.95
        if glava.distance(275, -175) < glava.radius + 25:
            print("win")
            LEVEL = 2
            COSTUME = 1
            draw_level(LEVEL, COSTUME)
    if level == 2:
        if costume == 1:
            if glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200 and glava.xcor() - glava.radius < -100 or glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200 and glava.xcor() + glava.radius > 200 and glava.xcor() - glava.radius < 400:
                glava.yvelocity = glava.yvelocity * glava.bounce
            if glava.xcor() - glava.radius <= -400:
                glava.xvelocity = glava.xvelocity * -0.95
            if glava.xcor() >= 500:
                COSTUME = 2
                draw_level(LEVEL, COSTUME)
        if costume == 2:
            if glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200 and glava.xcor() - glava.radius < 200 and glava.xcor() + glava.radius > -400:
                glava.yvelocity = glava.yvelocity * glava.bounce
            if glava.distance(275, -175) < glava.radius + 25:
                print("win")
                LEVEL = 3
                COSTUME = 1
                draw_level(LEVEL, COSTUME)
    if level == 3:
        if glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200 and glava.xcor() - glava.radius < -100 and glava.xcor() - glava.radius > -400 and glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200:
            glava.yvelocity = glava.yvelocity * glava.bounce
        if glava.xcor() + glava.radius > 200 and glava.xcor() - glava.radius < 400 and glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200:
            glava.yvelocity = -7
        if glava.xcor() - glava.radius <= -500 or glava.xcor() + glava.radius >= 500:
            glava.xvelocity = glava.xvelocity * -0.95
        if glava.ycor() + glava.radius >= 250 and glava.ycor() - glava.radius <= 300 and glava.xcor() - glava.radius < 100 and glava.xcor() + glava.radius > -300:
            glava.yvelocity = glava.yvelocity * glava.bounce
        if glava.distance(-375, 275) < glava.radius + 25:
            print("win")
            LEVEL = 4
            COSTUME = 1
            draw_level(LEVEL, COSTUME)
    if level == 4:
        if glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200 and glava.xcor() - glava.radius < -100 and glava.xcor() + glava.radius > -400 or glava.ycor() - glava.radius <= -150 and glava.ycor() >= -200 and glava.xcor() + glava.radius > 100 and glava.xcor() - glava.radius < 300:
            glava.yvelocity = glava.yvelocity * glava.bounce
        if glava.xcor() - glava.radius <= -500 or glava.xcor() + glava.radius >= 450 and glava.ycor() + glava.radius <= 250:
            glava.xvelocity = glava.xvelocity * -0.95
        if glava.ycor() + glava.radius >= -200 and glava.ycor() - glava.radius <= -150 and glava.xcor() - glava.radius < 300 and glava.xcor() + glava.radius > 100:
            glava.yvelocity = -8
        if glava.ycor() + glava.radius >= 250 and glava.ycor() - glava.radius <= 300 and glava.xcor() - glava.radius < 510 and glava.xcor() + glava.radius > 0 or glava.ycor() + glava.radius >= 400:
            glava.yvelocity = glava.yvelocity * glava.bounce
        if glava.xcor() + glava.radius >= 0 and glava.ycor() + glava.radius >= 240 and glava.ycor() - glava.radius <= 290 and glava.xcor() - glava.radius < 10:
            glava.xvelocity = glava.xvelocity * -0.95
        if glava.distance(375, 350) < glava.radius + 25:
            print("win")
            LEVEL = 1
            COSTUME = 1
            draw_level(LEVEL, COSTUME)




draw_level(LEVEL, COSTUME)
ekran.update()
ekran.listen()
ekran.onkeypress(lambda: move(0.4),"d")
ekran.onkeypress(lambda: move(-0.4),"a")
ekran.onkeypress(lambda: move(0.4),"Right")
ekran.onkeypress(lambda: move(-0.4),"Left")


while True:
    ekran.update()


    colision(LEVEL, COSTUME)

    glava.yvelocity += glava.gravity
    glava.xvelocity *= 0.95
    glava.sety(glava.ycor() - glava.yvelocity)
    glava.setx(glava.xcor() + glava.xvelocity)

    time.sleep(1 / FPS)
