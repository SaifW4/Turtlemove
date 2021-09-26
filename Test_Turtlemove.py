import turtle

import Turtlemove


def test_turtle_move():
    Turtlemove.turtle_move(50,80)
    assert(turtle.xcor()==50)
    assert(turtle.ycor()==80)







