#!/usr/bin/python
#encoding:utf-8
import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.IN)
GPIO.setup(12,GPIO.IN)
status1 = False
status2 = False

former1 = False
former2 = False

pygame.mixer.init()


while(1):
    if GPIO.input(12) == True and status2 == False:
        status1 = True
        former1 = True
        print("1")
        continue
    elif GPIO.input(12) == True and status2 == True and former1 == False:
        status2 = False
        status1 = False
        former1 = True
        former2 = True
        print("1")
        pygame.mixer.music.load('/home/pi/test/web/static/uploads/1.mp3')
        pygame.mixer.music.play()
        continue
    elif GPIO.input(38) == True and status1 == False:
        status2 = True
        former2 = True
        print("2")
        continue
    elif GPIO.input(38) == True and status1 == True and former2 == False:
        status1 = False
        status2 = False
        former1 = True
        former2 = True
        print("2")
        pygame.mixer.music.load('/home/pi/test/web/static/uploads/2.mp3')
        pygame.mixer.music.play()
        continue
    elif GPIO.input(38) == False and GPIO.input(12) == False:
        former1 = False
        former2 = False
    else:
        print("000")
GPIO.cleanup()
GPIO.cleanup()