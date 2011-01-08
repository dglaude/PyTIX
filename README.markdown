PyTIX is an implementation of the TIX LED clock in Python. It uses [curses][1] to draw the clock to a terminal window.

##Usage

`python pytix_c.py [update interval, defaults to 4 seconds]`

##Interpretation

Count the groups of colored squares from left to right to get the time&mdash;e.g., 1x red (left), 2x green, 3x blue, 4x red(right) means it is 12:34.

##Quitting

`Ctrl-C` at the moment.

[1]: http://docs.python.org/library/curses.html
