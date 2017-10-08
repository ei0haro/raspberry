from __future__ import division
import os
import time
from demo_opts import get_device
from luma.core.virtual import terminal
from luma.core.render import canvas
from PIL import ImageFont
import xbox
import Adafruit_PCA9685

#CONSTANTS
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
xBoxMin = -1
xBoxMax = 1

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)


def draw_text(x, y, text):
    with canvas(device) as draw:
        if text:
            draw.text((x, y), str(text), font=usedfont, fill=255)
        else:
            draw.point((x, y), fill=255)


def mapXCoordinate(x):
    oledXMax = device.width - 1
    oledXMin = 1
    return (((x - xBoxMin) * (oledXMax - oledXMin)) / (xBoxMax - xBoxMin)) + oledXMin


def mapYCoordinate(y):
    oledYMax = 1
    oledYMin = device.height - 1
    return (((y - xBoxMin) * (oledYMax - oledYMin)) / (xBoxMax - xBoxMin)) + oledYMin


def mapXboxToToPWM(y):
    pwmMapped = (((y - xBoxMin) * (servo_max - servo_min)) / (xBoxMax - xBoxMin)) + servo_min
    return int(round(pwmMapped))

def menuChoice():
    term.clear()
    term.println("Press key to continue...")
    term.println("Back: Exit Program")
    term.println("A: Control Servo")
    term.println("Y: Control LED")

    xBoxKeyPressed = ""
    while not xBoxKeyPressed:
        if joy.A():
            xBoxKeyPressed = "A"
        if joy.Y():
            xBoxKeyPressed = "Y"
        if joy.Back():
            xBoxKeyPressed = "Back"
        time.sleep(0.3)

    return xBoxKeyPressed


def LEDMode():
    while not joy.Back():

        text = ""
        if joy.A():
            text += "A"
        if joy.B():
            text += "B"
        if joy.Y():
            text += "Y"
        if joy.X():
            text += "X"

        x, y = joy.leftStick()
        draw_text(mapXCoordinate(x), mapYCoordinate(y), text)


def servoMode():
    term.println("Press Back to go to menu")
    while not joy.Back():
        x, y = joy.leftStick()
        pwm.set_pwm(0, 0, mapXboxToToPWM(x))
        pwm2.set_pwm(15, 0, mapXboxToToPWM(y))


def main():
    xBoxKeyPressed = ""
    while not xBoxKeyPressed == "Back":

        xBoxKeyPressed = menuChoice()
        if xBoxKeyPressed == "A":
            servoMode()
        elif xBoxKeyPressed == "Y":
            LEDMode()
    joy.close()

if __name__ == "__main__":

    try:
        usedfont = make_font("C&C Red Alert [INET].ttf", 10)
        device = get_device()
        term = terminal(device, usedfont)

        term.animate = False
        term.println("Connecting to XBOX Controller...")
        joy = xbox.Joystick()
        term.println("SUCCESS")
        time.sleep(1.0)

        pwm = Adafruit_PCA9685.PCA9685()
        pwm2 = Adafruit_PCA9685.PCA9685(address=0x41)

        pwm.set_pwm_freq(60)
        pwm2.set_pwm_freq(60)

        main()
    except KeyboardInterrupt:
        pass
