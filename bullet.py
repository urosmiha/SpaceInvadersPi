import turtle

class Bullet():

    bullet = turtle.Turtle()
    speed = 10
    size_x = 0.2
    size_y = 0.5
    shape = "square"
    colour = "yellow"
    orientation = 90

    fired = True

    def __init__(self):
        print("Bullet Ready")

    def render_bullet(self):
        self.bullet.color(self.colour)
        self.bullet.shape(self.shape)
        self.bullet.penup()
        self.bullet.speed(0)
        self.bullet.setheading(self.orientation)
        self.bullet.shapesize(self.size_x, self.size_y)
        self.bullet.hideturtle()

    def move(self):
        if self.fired:
            y = self.bullet.ycor()
            y += self.speed
            self.bullet.sety(y)

            if y > 280:
                fired = False
                self.bullet.hideturtle()

    def fire(self, pl_pos_x, pl_pos_y):
        # if self.bullet.xcor() > 280:
        self.bullet.setposition(pl_pos_x, pl_pos_y + 10)
        self.bullet.showturtle()

