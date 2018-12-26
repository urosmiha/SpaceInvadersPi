import turtle
import os

BORDER_RIGHT = 600
BORDER_LEFT = 90

def setup_screen():
    """Create a main screen."""
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Space Invaders")
    _draw_border()


def _draw_border():
    """Draw border on the main window."""
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(BORDER_RIGHT)
        border_pen.lt(BORDER_LEFT)
    border_pen.hideturtle()