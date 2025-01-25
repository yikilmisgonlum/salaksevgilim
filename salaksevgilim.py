#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time
import math

ASKIM = [
"⠀⠀⠀⠀⠀⠀⠀Bu kiz sen               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⢀⡤⠔⠒⠚⠉⠉⠉⠉⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠰⡏⠉⠀⠀⠀⠀⠈⠉⠒⢤⡀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⣀⡀⠙⡖⡇⠀⠀⠀⠀⠀⠀⠀⢀⠜⠑⠒⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠣⠈⢢⠟⠞⠁⠀⠀⠀⠀⣀⠴⣋⠀⠀⠀⠀⠀⠉⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⣀⡠⠴⠋⠑⠢⠤⠤⠤⠤⠐⠚⠛⢗⠒⠒⠂⠙⠳⠤⡀⠀⠉⠢⡀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀",
"⠘⠿⣍⣁⣀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢿⢆⠀⠀⠀⠀⠈⠑⢄⠀⠈⢢⡀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀",
"⠀⠀⠀⢨⠃⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⡴⡱⠁⠀⠉⠢⢄⣀⠀⠀⠀⠑⢄⠀⠱⡀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀",
"⠀⠀⢠⠃⢀⣖⠤⢄⣀⠀⠀⡗⢦⡀⠀⡜⡜⠀⠀⠀⠀⠀⣼⡏⠉⠐⠒⠠⠬⣦⠀⠱⡀⠀⠀⠀⢸⠀⠀⠀⠀⠀",
"⠀⢀⡏⠀⣸⣦⢍⣐⡚⠛⣻⠃⠀⠈⠲⠾⣀⡀⠀⠀⠀⢰⢿⢀⡠⢄⡀⠀⠀⠀⢣⠀⢱⠀⠀⠀⢸⠀⠀⠀⠀⠀",
"⠀⣸⠀⣰⡏⠸⠉⠒⠛⠛⡟⠒⠉⠁⠀⠀⠀⠉⠁⠒⠒⠾⠦⠬⡤⠤⠤⠄⢠⠐⠘⣇⠈⡆⠀⠀⢸⠀⠀⠀⠀⠀",
"⠀⣇⡴⢁⠇⡇⠀⠀⠀⣸⠀⢀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣷⣦⣄⣸⠆⠀⢸⡀⣿⣄⠀⢸⠀⠀⠀⠀⠀",
"⠀⠿⠀⢸⠀⡇⠀⠀⠀⣧⣴⣿⡿⠛⢻⣧⠀⠀⠀⠀⠀⠀⢰⠋⠀⣹⣿⣿⣿⠃⠀⠀⢿⣿⣿⠀⢸⠀⠀⠀⠀⠀",
"⠀⠀⠀⢸⠀⡇⠀⠀⢀⢿⠸⣿⠇⠠⠾⢿⠀⠀⠀⠀⠀⠀⡜⠒⠊⠉⠉⢹⠙⠀⠀⠀⡞⣿⣿⠁⠘⡆⠀⠀⠀⠀",
"⠀⠀⠀⠸⣷⣧⠀⠀⢸⠀⡇⠸⡄⠀⠀⠀⡇⠀⠀⠀⠀⠀⠹⡀⠀⠀⢀⡞⡇⠀⠀⣰⠷⠟⠁⠀⠀⢻⠀⠀⠀⠀",
"⠀⠀⠀⠀⢻⠿⡀⠀⢻⠀⡇⠀⠱⢄⣀⠜⠁⠀⠀⠀⠀⠀⠀⠉⠒⠒⠊⢠⠃⠀⢠⠃⠀⠀⢠⠀⠀⠀⢧⠀⠀⠀",
"⠀⠀⠀⠀⡞⠀⠙⢄⢸⠀⣧⡀⠀⠀⠀⠀⠀⠀⡔⠉⠱⡀⠀⠀⠀⠀⠀⡜⠀⡠⠃⠀⠀⠀⣧⣀⠀⠀⠈⢧⠀⠀",
"⠀⠀⠀⡸⠀⢰⡄⠈⠙⠇⢻⣏⡒⠤⢀⣀⣀⣀⠙⣦⣔⣁⣀⣀⡠⠤⢾⢃⠜⠁⠀⡇⠀⣸⠁⠈⠉⠒⠢⠤⢷⠄",
"⠀⠀⢰⠷⠊⠁⠳⡄⠀⠀⠀⢩⠙⠳⢶⣖⡆⣠⣿⢛⣻⣿⣿⣿⣦⠀⢸⣍⠀⢀⠞⢳⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⢀⣾⠀⡰⢻⣀⡴⣿⣿⠿⣿⠻⣯⠀⢹⣷⣏⢹⡶⠋⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠚⠘⠋⠀⣾⡁⢀⣨⡇⠀⠈⡆⠹⡇⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
]

BEN = [
"  ___ ",
" (o-o)",
"  -v- ",
"  / \ "
]

SPEECH_BUBBLE = [
"   ____________",
"  /            \\",
" < ❤️❤️❤️       >",
" < - ben        >",
"  \\____________/"
]

def draw_multiline(stdscr, start_y, start_x, lines):
    for i, line in enumerate(lines):
        stdscr.addstr(start_y + i, start_x, line)

def main(stdscr):
    curses.curs_set(0)          # İmleci gizle
    stdscr.nodelay(False)
    stdscr.clear()

    # Terminal boyutu
    max_y, max_x = stdscr.getmaxyx()

    girl_height = len(ASKIM)
    girl_width = max(len(line) for line in ASKIM)
    girl_start_y = 2
    girl_start_x = 2

    draw_multiline(stdscr, girl_start_y, girl_start_x, ASKIM)

    radius = 10
    girl_center_y = girl_start_y + girl_height // 2
    girl_center_x = girl_start_x + girl_width // 2

    angle = 0
    try:
        while True:
            stdscr.clear()
            draw_multiline(stdscr, girl_start_y, girl_start_x, ASKIM)

            rad = math.radians(angle)
            child_y = int(girl_center_y + radius * math.sin(rad))
            child_x = int(girl_center_x + radius * math.cos(rad))

            draw_multiline(stdscr, child_y, child_x, BEN)

            bubble_offset_x = 6
            bubble_offset_y = -2  # YUKARI
            draw_multiline(
                stdscr,
                child_y + bubble_offset_y,
                child_x + bubble_offset_x,
                SPEECH_BUBBLE
            )

            stdscr.refresh()
            time.sleep(0.15)  # animasyon hızı

            angle += 10
            if angle >= 360:
                angle = 0

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    curses.wrapper(main)



