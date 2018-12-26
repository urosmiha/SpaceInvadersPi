import turtle

class Player():

    player = turtle.Turtle()
    speed = 15
    pos_x = 0
    pos_y = -250
    shape = "triangle"
    colour = "blue"
    orientation = 90

    def __init__(self):
        print("Player One Ready")

    def render_player(self):
        self.player.color(self.colour)
        self.player.shape(self.shape)
        self.player.penup()
        self.player.speed(self.speed)
        self.player.setposition(self.pos_x, self.pos_y)
        self.player.setheading(self.orientation)

    def move_right(self):
        x = self.player.xcor()
        x += self.speed
        if x > 280:
            x = 280
        else:
            self.player.setx(x)

    def move_left(self):
        x = self.player.xcor()
        x -= self.speed
        if x < -280:
            x = -280
        else:
            self.player.setx(x)
