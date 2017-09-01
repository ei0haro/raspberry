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
from PIL import ImageFont
import xbox


def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)


def main():

    term = terminal(device, make_font("tiny.ttf", 8), "white", "black", 4, None, False)
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

    joy.close()



if __name__ == "__main__":

    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
