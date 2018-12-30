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


def check_player_dead(enemy_one):
    if enemy_one.enemy.ycor() < -200:
        return True
    return False


if __name__ == "__main__":

    main_window.setup_screen()

    player_one = player.Player()
    player_one.render_player()

    # enemy_one = enemy.Enemy(-200, 200)
    # enemy_two = enemy.Enemy(100, 200)


    speed = 2.0
    speed_up = 1.0
    pos_x = -200
    pos_y = 250
    shape = "square"
    colour = "red"
    orientation = 90

    for enemy_unit in range(5):
        enemy = turtle.Turtle()
        pos_x += 50
        # pos_y = 250
        pos_x = pos_x
        pos_y = pos_y
        enemy.color(colour)
        enemy.shape(shape)
        enemy.penup()
        # Drawing speed
        enemy.speed(1)
        enemy.setposition(pos_x, pos_y)
        enemy.setheading(orientation)
        enemy.speed(0)

    # enemies = [20]


    turtle.listen()
    turtle.onkey(player_one.move_right, "Right")
    turtle.onkey(player_one.move_left, "Left")
    turtle.onkey(player_one.fire_bullet, "space")

    while True:
        player_one.move()
        # enemy_one.move()
        # enemy_two.move()

        # pl_bullet_x, pl_bullet_y = player_one.get_bullet_cor()

        # if check_collision(pl_bullet_x, enemy_one.enemy.xcor(),
        #                    pl_bullet_y, enemy_one.enemy.ycor()):
        #     enemy_one.reset()

        # if check_player_dead(enemy_one):
        #     print "THE END"
        #     exit(0)

        # if check_collision(player_one.player.xcor(),enemy_one.enemy.xcor(),
        #                     player_one.player.xcor(), enemy_one.enemy.ycor()):
        #     exit(0)
