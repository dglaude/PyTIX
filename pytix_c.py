#!/usr/bin/env python

# Displays the TIX clock using Curses
# 2007-02-16

# Usage: pytix_c.py [update interval]

import sys, time, random, curses

assert sys.version >= '2.3', "Python 2.3 or later required."

try: inter = int(sys.argv[1])
except: inter = 4		# default update interval (secs)

def tog(start, end, n, col = 2):
	"Toggle on n values randomly in the array between start and end."
	global disp

	for z in random.sample(range(3 * (end - start)), n):
		disp[z % 3][start + z // 3] = col

def getsym(n):
	"Return the on/off LED symbol."
	if n > 2: return ' '
	elif n == 1: return ':'
	else: return '+'

def mainprog(win):
	global disp

	assert curses.has_colors(), "Your terminal does not support colors."
	try: curses.curs_set(0)
	except: pass
	boxx, boxy = win.getmaxyx()[1] // 16, win.getmaxyx()[0] // 10

	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
	curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
	curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)

	while True:
		t = time.strftime("%I%M", time.localtime())
		h1, h2, m1, m2 = [int(x) for x in t]
		disp = [[2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2] for y in range(3)]
		tog(0, 1, h1, 3)
		tog(2, 5, h2, 4)
		tog(6, 8, m1, 5)
		tog(9, 12, m2, 3)
		for x in range(12):
			for y in range(3):
				for yy in range(boxy):
					win.addstr(y * (boxy + 1) + yy + boxy,
						x * (boxx + 1) + boxx,
						boxx * getsym(disp[y][x]),
						curses.color_pair(disp[y][x]))
		win.move(0, 0)
		win.refresh()
		time.sleep(inter)

curses.wrapper(mainprog)

