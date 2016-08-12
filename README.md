PyTIX is an implementation of the TIX LED clock in Python.

The [original version](https://github.com/mdoege/PyTIX) used [curses](http://docs.python.org/library/curses.html) to draw the clock to a terminal window.
This version use the [mote](https://github.com/pimoroni/mote) library to display the time.
Require mote hardware from Pimoroni.

##Usage

`python pytix_mote.py [update interval, defaults to 1 seconds] ["--12" for 12-hour mode]`

##Interpretation

Count the groups of colored squares from left to right to get the time&mdash;e.g., 1x red (left), 2x green, 3x blue, 4x red(right) means it is 12:34.

##Quitting

`Ctrl-C` at the moment.

