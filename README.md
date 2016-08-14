#PyTIX, an implementation of the TIX LED clock in Python

![screenshot](https://github.com/mdoege/PyTIX/raw/master/screenshot.png "PyTIX screenshot")
_11:53…_

It can either use [curses](http://docs.python.org/library/curses.html) to draw the clock to a terminal window or use the [mote](https://github.com/pimoroni/mote) library to display the time. (Requires mote hardware from Pimoroni.)

##Usage

`python pytix.py [update interval, defaults to 4 seconds] ["--24" for 24-hour mode]`

`python pytix_mote.py [update interval, defaults to 1 second] ["--12" for 12-hour mode]`

##Interpretation

Count the groups of colored squares from left to right to get the time&mdash;e.g., 1x red (left), 2x green, 3x blue, 4x red(right) means it is 12:34.

##Quitting

`Ctrl-C`

