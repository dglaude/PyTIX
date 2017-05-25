#!/usr/bin/env python

# Displays the TIX clock using Curses
# 2011-01-08

# Modified to use mote by David Glaude
# Modified for my prefered default value: 1 second update and 24 Hours
# 2016-08-12

# Modified to use sense HAT by David Glaude
# 2017-05-25

# Usage: pytix_sense.py [update interval] [--12]

import sys, time, random

try:
    from sense_hat import SenseHat
except ImportError:
    exit("This script requires the sense_hat module\nInstall with: apt-get install sense-hat")

assert sys.version >= '2.3', "Python 2.3 or later required."

try: inter = int(sys.argv[1])
except: inter = 1		# default update interval (secs)

if '--24' in sys.argv:
	f = '%I%M'
else:
	f = '%H%M'

colors = [
    (  0,   0,   0),  # Unused position in the colour table
    (  0,   0,   0),  # 1 Colour for unused position between digit
    (  1,   0,   0),  # 2 OFF Colour for hours first digit = RED
    (255,   0,   0),  # 3 ON  Colour for hours first digit = RED
    (  0,   1,   0),  # 4 OFF Colour for hours second digit = GREEN
    (  0, 255,   0),  # 5 ON  Colour for hours second digit = GREEN
    (  0,   0,   1),  # 6 OFF Colour for minutes first digit = BLUE
    (  0,   0, 255),  # 7 ON  Colour for minutes first digit = BLUE
    (  1,   0,   0),  # 8 OFF Colour for minutes first digit = BLUE
    (255,   0,   0)   # 9 ON  Colour for minutes last digit = RED
]


def tog(level, start, end, n, col = 2):
	"Toggle on n values randomly in the array between start and end."
	global disp

	for z in random.sample(range(3 * (end - start)), n):
		disp[level + (z % 3)][start + z // 3] = col


def mainprog():
	"Display current time with pixels on a Sense HAT."
	global disp,sense

	t = time.strftime(f, time.localtime())
	h1, h2, m1, m2 = [int(x) for x in t]
	disp = [[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 2, 1, 4, 4, 4, 1],
		[1, 1, 2, 1, 4, 4, 4, 1],
		[1, 1, 2, 1, 4, 4, 4, 1], 
		[1, 1, 1, 1, 1, 1, 1, 1],
		[1, 6, 6, 1, 8, 8, 8, 1],
		[1, 6, 6, 1, 8, 8, 8, 1],
		[1, 6, 6, 1, 8, 8, 8, 1]] 
	tog(1, 2, 3, h1, 3)
	tog(1, 4, 7, h2, 5)
	tog(5, 1, 3, m1, 7)
	tog(5, 4, 7, m2, 9)

	for x in range(8):
		for y in range(8):
			r, g, b = colors[ disp[y][x] ]
			sense.set_pixel(x, y, r, g, b)

sense = SenseHat()
sense.set_rotation(0)
sense.clear()

try:
    while True:
        mainprog()
        time.sleep(inter)

except KeyboardInterrupt:
    sense.clear()
    time.sleep(0.1)

