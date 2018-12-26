import turtle


class Enemy():

    enemy = turtle.Turtle()
    speed = 2
    pos_x = -200
    pos_y = 250
    shape = "square"
    colour = "red"
    orientation = 90

    def __init__(self):
        print("Player One Ready")

    def render_enemy(self):
        self.enemy.color(self.colour)
        self.enemy.shape(self.shape)
        self.enemy.penup()
        self.enemy.speed(self.speed)
        self.enemy.setposition(self.pos_x, self.pos_y)
        self.enemy.setheading(self.orientation)

    def move(self):
        x = self.enemy.xcor()
        x += self.speed
        self.enemy.setx(x)