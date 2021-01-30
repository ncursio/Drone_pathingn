"""""
This is the main keyboard control system for the tello drone, this will facilitate 
the control of the tello drone through the pygame interface. 
"""""

from djitellopy import tello
import Keypress as kp
from time import sleep
import cv2
"""""
These are the list of libraries needed to make the program run if you do not knot have
have these view : https://www.youtube.com/watch?v=LmEcyQnfpDA&t=687s to see how to 
get them installed and to see a better explanation of the code.  
"""""

kp.init()
me = tello.Tello() # The creation of a tell object from the tello class imported to have access to the build in functions
me.connect() #This is one of the most important function, used to connect the computer to the drone
print(me.get_battery()) # generic battery percentage displayed to the screen

me.streamon() # this function allows us to get access from the tello drone's camera

"""""
These are the buttons on your keyboard that you will interact with to control the 
tello drone just keep in mind the yv which are denoted by 'a' & 'd' control the rotation
NOT the drone movement 'a' rotates to the left 'd' rotates to the right
"""""

def getKeyboardInput():
    lr,fb,ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("RIGHT"):lr = speed
    elif kp.getKey("LEFT"): lr = -speed

    if kp.getKey("UP"):fb = speed
    elif kp.getKey("DOWN"):fb = -speed

    if kp.getKey("w"):ud = speed
    elif kp.getKey("s"):ud = -speed

    if kp.getKey("a"):yv = -speed
    elif kp.getKey("d"):yv = speed

    if kp.getKey("q"): tl = me.takeoff() ,sleep(3) # this function allows us to get the tello drone to take off
    if kp.getKey("e"): tl = me.land() # this function allows us to get the tello drone to land

    return [lr, fb, ud, yv]

"""""
This is last while loop now is where the console is displayed and allow you to the live stream in one window and 
control the tello drone from a pygame window. 
"""""
while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    """""
    The above function is what receive the key inputs vals[0] controls 'left or right', vals[1] controls 'forward or backwards'
    vals[2] controls 'up or down',vals[3] controls 'left rotation or right rotation'
    """""
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)