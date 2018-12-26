import turtle


class Enemy():

    enemy = turtle.Turtle()
    speed = 2.0
    speed_up = 1.0
    pos_x = -200
    pos_y = 250
    shape = "square"
    colour = "red"
    orientation = 90

    def __init__(self):
        print("Enemy One Ready")

    def render_enemy(self):
        self.enemy.color(self.colour)
        self.enemy.shape(self.shape)
        self.enemy.penup()
        # Drawing speed
        self.enemy.speed(1)
        self.enemy.setposition(self.pos_x, self.pos_y)
        self.enemy.setheading(self.orientation)

    def drop_down(self):
        y = self.enemy.ycor()
        y += 5
        self.enemy.sety(y)

    def move(self):
        x = self.enemy.xcor()
        x += self.speed

        if x > 280 or x < -280:
            self.speed *= -1
            # self.speed = (-1 * self.speed) + self.speed_up
            y = self.enemy.ycor()
            y -= 40
            self.enemy.sety(y)

        self.enemy.setx(x)
