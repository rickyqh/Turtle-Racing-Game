import turtle
import random
TRACK_X = -350
TRACK_Y =200
TRACK_LEN = 700
TRACK_WIDTH = 400
LANE_WIDTH = 100
FINISH_X=250

def screen_setup():
    global turt
    screen=turtle.getscreen()
    screen.setup(800,500)
    screen.title("Turtle racing game")
    screen.bgcolor("#9F4123")
    turt=turtle.getturtle()
    turt.hideturtle()
    turt.speed(000000000000000000000000000)
    turt.penup()
    turt.goto(-100,205)
    turt.color("white")
    turt.write("Racing Turtles",font=("ariel",20,'bold'))

def draw_track():
    turt.goto(TRACK_X,TRACK_Y)
    turt.pendown()
    turt.fillcolor("chocolate")
    turt.begin_fill()
    for i in range(2):
        turt.forward(TRACK_LEN)
        turt.right(90)
        turt.forward(TRACK_WIDTH)
        turt.right(90)
    turt.end_fill()

    y=TRACK_Y-LANE_WIDTH
    for i in range(3):
        turt.goto(TRACK_X,y)
        turt.pendown()
        turt.forward(TRACK_LEN)
        y-=100
        turt.penup()


def draw_finishline():
    turt.penup()
    turt.goto(FINISH_X,TRACK_Y)
    turt.width(10)
    turt.right(90)
    turt.pendown()
    turt.forward(TRACK_WIDTH)

def create_turtles():
    global turt1
    global turt2
    global turt3
    global turt4
    turt1=turtle.Turtle()
    turt2=turtle.Turtle()
    turt3=turtle.Turtle()
    turt4=turtle.Turtle()

def setup_turtles():

    turt1.reset()
    turt2.reset()
    turt3.reset()
    turt4.reset()

    turt1.color("#FFD700")
    turt2.color("red")
    turt3.color("#1598FF")
    turt4.color("lime")

    turt1.penup()
    turt2.penup()
    turt3.penup()
    turt4.penup()

    turt1.goto(-300,150)
    turt2.goto(-300,50)
    turt3.goto(-300,-50)
    turt4.goto(-300,-150)

    turt1.shape("turtle")
    turt2.shape("turtle")
    turt3.shape("turtle")
    turt4.shape("turtle")

    turt1.pendown()
    turt2.pendown()
    turt3.pendown()
    turt4.pendown()

def get_guess():
    return int(turtle.textinput("guess","Guess which turtle 1,2,3 or 4 will win."))

def check_guess(get_guess, winner):
    if get_guess==winner:
        a=turtle.textinput("You win",f'turtle {winner} won the game. Enter stop to stop,enter redo to play again')
    else:
        a=turtle.textinput("You lose",f'turtle {winner} won the game. Enter stop to stop,enter redo to play again')
    



def race():

    guess = get_guess() 

    while turt1.xcor()<= FINISH_X and turt2.xcor()<= FINISH_X and turt3.xcor()<= FINISH_X and turt4.xcor()<= FINISH_X:
        turt1.forward(random.randint(1,10))
        turt2.forward(random.randint(1,10))
        turt3.forward(random.randint(1,10))
        turt4.forward(random.randint(1,10))

    if turt1.xcor()>=FINISH_X:
        winner=1
    elif turt2.xcor()>=FINISH_X:
        winner=2
    elif turt3.xcor()>=FINISH_X:
        winner=3
    elif turt4.xcor()>=FINISH_X:
        winner=4

    check_guess(guess, winner)




    
    


def main():
    screen_setup()
    draw_track()
    draw_finishline()
    create_turtles()
    while True:
        setup_turtles()
        race()


if __name__== "__main__":
    main()
