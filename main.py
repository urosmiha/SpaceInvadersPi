import turtle
import os
import time
import math

import main_window
import player
import enemy

def test():
    print "Hello"
    return


def check_collision(x_1, x_2, y_1, y_2):
    x_pow = math.pow(x_1 - x_2, 2)
    y_pow = math.pow(y_1 - y_2, 2)
    distance = math.sqrt(x_pow + y_pow)

    if distance < 15:
        return True
    return False


if __name__ == "__main__":

    main_window.setup_screen()

    player_one = player.Player()
    player_one.render_player()

    enemy_one = enemy.Enemy()
    enemy_one.render_enemy()

    turtle.listen()
    turtle.onkey(player_one.move_right, "Right")
    turtle.onkey(player_one.move_left, "Left")
    turtle.onkey(player_one.fire_bullet, "space")

    while True:
        player_one.move()
        enemy_one.move()
        # if check_collision(player_one.bullet.bullet.xcor(), enemy_one.enemy.xcor(),
        #                     player_one.bullet.bullet.ycor(), enemy_one.enemy.ycor()):
