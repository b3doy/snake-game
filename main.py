from turtle import Screen
import time
from oray import Oray
from parab import Parab
from papanskor import Papanskor


# setup the screen
layar = Screen()
layar.setup(width=600, height=600)
layar.bgcolor("black")
layar.title("Oray Virtual")
layar.tracer(0)
# assigment snake object to Class 
oray = Oray()
parab = Parab()
papanskor = Papanskor()

# Assign the control

layar.listen()
layar.onkey(key="Up", fun=oray.up)
layar.onkey(key="Down", fun=oray.down)
layar.onkey(key="Left", fun=oray.left)
layar.onkey(key="Right", fun=oray.right)

# game's on
game_on = True
while game_on:
    layar.update()
    time.sleep(0.1)    
    oray.move()
    # detect collision with the food
    if oray.hulu.distance(parab) < 15:
        parab.refresh()
        oray.extend()
        papanskor.tambah_skor()
    
    # detect collision with the wall
    if oray.hulu.xcor() > 290 or oray.hulu.xcor() < -290 or oray.hulu.ycor() > 290 or oray.hulu.ycor() < -290:
        game_on = False
        papanskor.game_over()
    
    # detect collision with the tail
    for body in oray.orays[1:]:
        if oray.hulu.distance(body) < 10:
            game_on = False
            papanskor.game_over()
        



layar.exitonclick()

