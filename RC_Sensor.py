 #!/usr/bin/env python
import pygame
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#--------Below is the initializtion--------

#Initialize the pygame library
pygame.init()

#Set the GPIO
GPIO.setwarnings(False)

#Connect to the controller
ps4 = pygame.joystick.Joystick(0)

#Setting motor to Pi pins
Motor1A = 13
Motor1B = 15
Motor1E = 11
Servo1Y = 29
Servo1R = 31

#Setting motor/servo as output
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Servo1Y,GPIO.OUT)
GPIO.setup(Servo1R,GPIO.OUT)

#Front Disatnce Sensor Setup
GPIO_TRIG = 23
GPIO_ECHO = 21
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#Left Distance Sensor
GPIO_TRIGL = 37
GPIO_ECHOL = 35
GPIO.setup(GPIO_TRIGL, GPIO.OUT)
GPIO.setup(GPIO_ECHOL, GPIO.IN)

#Right Distance Sensor
GPIO_TRIGR = 18
GPIO_ECHOR = 16
GPIO.setup(GPIO_TRIGR, GPIO.OUT)
GPIO.setup(GPIO_ECHOR, GPIO.IN)

#--------Below are the defined functions--------
"""------------Motor Functions--------------"""
#Backward function
def backward():
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    
#Stop function
def DStop():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)
    
#Forward function
def forward():
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    
def empty():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)

"""------------Servo Functions--------------"""
#Left function
def left():
    print("Go Left")
    GPIO.output(Servo1R, GPIO.HIGH)
    GPIO.output(Servo1Y, GPIO.LOW)
#Right function
def right():
    print("Go Right")
    GPIO.output(Servo1R, GPIO.LOW)
    GPIO.output(Servo1Y, GPIO.HIGH)
#Servo off function
def off():
    print("Servo is off")
    GPIO.output(Servo1R,GPIO.LOW)
    GPIO.output(Servo1Y,GPIO.LOW)
    
"""------------Distance Sensor Functions------------"""
#front distance sensor 
def distance():
    # set Trig to HIGH
    GPIO.output(GPIO_TRIG, True)
 
    # set Trig after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance


"""#Left Distance Sensor
def distanceL():
    # set Trig to HIGH
    GPIO.output(GPIO_TRIGL, True)
 
    # set Trig after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGL, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHOL) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHOL) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distanceL = (TimeElapsed * 34300) / 2
 
    return distanceL

#Right Distance Sensor
def distanceR():
    # set Trig to HIGH
    GPIO.output(GPIO_TRIGR, True)
 
    # set Trig after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGR, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHOR) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHOR) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distanceR = (TimeElapsed * 34300) / 2
 
    return distanceR"""

"""-------------------Main Loop-------------------"""
#Sleep at the start of the program
#time.sleep(2)
print ("Program Start!!!")

while True:
    #Check event and controller each time
    pygame.event.get()
    ps4.init()
    #dist = distance()
    """distL = distanceL()
    distR = distanceR()"""

    if ps4.get_button(7) == 0 & ps4.get_button(6) == 0:
        DStop()
    if ps4.get_button(7) == 1:
        forward()
    if ps4.get_button(6) == 1:
        backward()
        
    if ps4.get_button(1) == 0 & ps4.get_button(3) == 0:
        off()
    if ps4.get_button(1) == 1:
        right()
    if ps4.get_button(3) == 1:
        left()

    #Distance sensor
    """#print(ultrasonic.distance)
    dist = distance()
    print ("Measured Distance = %.1f cm" % dist)
    time.sleep(1)
    
    #print(ultrasonic.distance)
    distL = distanceL()
    print ("Measured DistanceL = %.1f cm" % distL)
    #time.sleep(1)"""

GPIO.cleanup()

