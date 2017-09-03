#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Simple println capabilities.
"""

import os
import time
from demo_opts import get_device
from luma.core.virtual import terminal
from luma.core.render import canvas
from PIL import ImageFont
import xbox


def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)

def draw_dot(x,y):
#   bbox = [(x, y), (x+1, y+1)]
   with canvas(device) as draw:
       draw.point((x,y), fill="#ddddff")
#       draw.rectangle(bbox, fill="#ddddff", outline="blue")

def mapXCoordinate(x):
   oledXMax=127
   oledXMin=1
   xBoxXMax=1
   xBoxXMin=-1
   return (((x - xBoxXMin) * (oledXMax - oledXMin)) / (xBoxXMax - xBoxXMin)) + oledXMin

def mapYCoordinate(y):
   oledYMax=1
   oledYMin=31
   xBoxYMax=1
   xBoxYMin=-1
   return (((y - xBoxYMin) * (oledYMax - oledYMin)) / (xBoxYMax - xBoxYMin)) + oledYMin

def main():

    term = terminal(device, make_font("tiny.ttf", 6), "white", "black", 4, None, False)
    term.println("Connecting to XBOX Controller...")
    joy = xbox.Joystick()
    term.println("SUCCESS")

    while not joy.Back():
    
        if joy.A():
            term.println("Button A Pressed")
        if joy.B():
            term.println("Button B Pressed")
        if joy.Y():
            term.println("Button Y Pressed")
        if joy.X():
            term.println("Button X Pressed")

	x, y = joy.leftStick()
	
	draw_dot(mapXCoordinate(x),mapYCoordinate(y))

    joy.close()



if __name__ == "__main__":

    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
