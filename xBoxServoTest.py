from __future__ import division
import os
import time
#from demo_opts import get_device
#from luma.core.virtual import terminal
#from luma.core.render import canvas
#from PIL import ImageFont
import xbox
import Adafruit_PCA9685


'''def make_font(name, size):
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
'''

def mapXboxToToPWM(y):
   xBoxYMax=1
   xBoxYMin=-1
   pwmMapped = (((y - xBoxYMin) * (servo_max - servo_min)) / (xBoxYMax - xBoxYMin)) + servo_min
   return int(round(pwmMapped)) 

def main():

#    term = terminal(device, usedfont)
#    term.animate=False
#    term.println("Connecting to XBOX Controller...")
    print "Connecting to XBOX...."
    joy = xbox.Joystick()
    print "SUCCESS"

#term.println("SUCCESS")

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
        if text:
	    print text
        x, y = joy.leftStick()

	pwm.set_pwm(0, 0, mapXboxToToPWM(x))
        pwm2.set_pwm(15, 0, mapXboxToToPWM(y))
#	draw_text(mapXCoordinate(x), mapYCoordinate(y), text)

    joy.close()



if __name__ == "__main__":

    try:
#        usedfont= make_font("tiny.ttf", 6)
#        device = get_device()
	pwm = Adafruit_PCA9685.PCA9685()
	pwm2 = Adafruit_PCA9685.PCA9685(address=0x41)
	servo_min = 150  # Min pulse length out of 4096
	servo_max = 600  # Max pulse length out of 4096
	pwm.set_pwm_freq(60)
        main()
    except KeyboardInterrupt:
        pass


