import turtle
import os

import main_window
import player
import enemy

def test():
    print "Hello"
    return

if __name__ == "__main__":

    main_window.setup_screen()

    player_one = player.Player()
    player_one.render_player()

    enemy_one = enemy.Enemy()
    enemy_one.render_enemy()

    turtle.listen()
    turtle.onkey(player_one.move_right, "Right")
    turtle.onkey(player_one.move_left, "Left")

    while True:
        enemy_one.move()
