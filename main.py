import turtle
import os

import main_window
import player

def test():
    print "Hello"
    return

if __name__ == "__main__":

    main_window.setup_screen()

    player_one = player.Player()
    player_one.render_player()

    turtle.listen()
    turtle.onkey(player_one.move_right, "Right")
    turtle.onkey(player_one.move_left, "Left")

    delay = raw_input("")
    pass
