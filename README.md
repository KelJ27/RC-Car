# Object Avoiding RC Car

# Table of Contents
* Introduction
* Parts List
* Features
* Setup

# Introduction
With the rapid change in technology, society has reached a point where the very cars we drive are automated, and can avoid collision. Making a car that has this functionality is quite a difficult task, therefore my partner and I decided to start small with an Object Avoiding RC Car. This car we designed functions like any regular RC car, but the difference is you can use a Bluetooth device to control it. The Bluetooth device we chose to interface with the Raspberry Pi was a Playstation 4 Controller, which allowed the car to move forward, backward, left, and right with just the push of a button. For collision avoidance, we placed sensors around the chassis of the car. This allowed the car to stop, or turn in the opposite direction of an object if that object is sensed at certain distances. 

![Alt Text](/images/RC_car.jpg)

# Parts List
* RC Car Chassis
* 7.4V DC Motor
* Positional Rotation Servo
* 2 Motor Drivers
* 3 Ultrasonic Distance Sensors
* DC-DC Adjustable Buck Converter
* Mini Solderless Breadboards
* 7.4V Battery
* 5V Power Bank
* Raspberry Pi 3
* Playstation Dualshock 4 Controller

### Software/Packages
* Pygame
* ds4drv
* Python 3 (IDLE)

# Setup

### Schematics

![Alt Text](/images/RC_car_schematic_1.png)


