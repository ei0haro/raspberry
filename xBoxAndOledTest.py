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

def draw_text(x, y, text):
   with canvas(device) as draw:
       if text:
           draw.text((x,y), str(text), font=usedfont, fill=255)
       else: draw.point((x,y), fill=255)

def mapXCoordinate(x):
   oledXMax = device.width-1
   oledXMin=1
   xBoxXMax=1
   xBoxXMin=-1
   return (((x - xBoxXMin) * (oledXMax - oledXMin)) / (xBoxXMax - xBoxXMin)) + oledXMin

def mapYCoordinate(y):
   oledYMax=1
   oledYMin = device.height-1
   xBoxYMax=1
   xBoxYMin=-1
   return (((y - xBoxYMin) * (oledYMax - oledYMin)) / (xBoxYMax - xBoxYMin)) + oledYMin

def main():

    term = terminal(device, usedfont)
    term.animate=False
    term.println("Connecting to XBOX Controller...")
    joy = xbox.Joystick()
    term.println("SUCCESS")

    while not joy.Back():
    
        text = ""
        if joy.A():
            text+="A"
        if joy.B():
            text+="B"
        if joy.Y():
            text+="Y"
        if joy.X():
            text+="X"

	x, y = joy.leftStick()
	
	draw_text(mapXCoordinate(x), mapYCoordinate(y), text)

    joy.close()



if __name__ == "__main__":

    try:
        usedfont= make_font("tiny.ttf", 6)
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
