import turtle
import random
import time

Screen = turtle.Screen()
Screen.bgcolor("light blue")
screen_width = Screen.window_width()
screen_height = Screen.window_height()
turtle.speed(0)
turtle.penup()

my_turtle = turtle.Turtle("turtle")
my_turtle.color("green")
my_turtle.shapesize(1.5)
my_turtle.penup()
my_turtle.speed(0)
score = 0
turtle.goto(0, screen_height / 2 - 60)
turtle.write(f"Score:{0}", False, "center", font=("Courier", 30))

game_over=False
def mouse_click(x, y):
    global  game_over
    if not game_over:
     print(f"mouse clicked {x, y}")
     my_turtle.penup()
     check_collision(x,y)
def check_collision(x, y):
    global score
    for t in turtle.Screen().turtles():
        if t.distance(x, y) < 20:
             print("Turtle collided!")
             my_turtle.goto(random.randint(0, 250), random.randint(0, 250))
             score += 1
             turtle.clear()
             turtle.write(f"Score:{score}", False, "center", font=("Courier", 30))


def on_mouse_click(x, y):
    print("Mouse clicked at:", x, y)
Screen.listen()
timer_text = turtle.Turtle()
screen_width = Screen.window_width()
screen_height = Screen.window_height()
turtle.speed(0)
start_time = time.time()
turtle.penup()
turtle.goto(0, screen_height / 2 - 60)
turtle.pendown()
turtle.hideturtle()
remaining_time = 20

while remaining_time > 0:
    timer_text.hideturtle()
    timer_text.penup()
    timer_text.speed("fastest")
    timer_text.clear()
    timer_text.goto(0, screen_height / 2 - 110)
    timer_text.write(int(remaining_time), font=("Courier", 30))
    Screen.update()
    remaining_time = 20 - (time.time() - start_time)
    time.sleep(1)
    timer_text.hideturtle()
    Screen.onscreenclick(mouse_click)
over=True
game_over=over
timer_text.clear()
timer_text.write("Game Over", font=("Courier", 30))
timer_text.goto(0, screen_height / 2 - 110)
time.sleep(2)
Screen.update()
turtle.mainloop()