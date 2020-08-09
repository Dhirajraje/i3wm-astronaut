#!/usr/bin/python3

import random, os, time

for i in time.asctime().split(' '):
	if ':' in i:
		turnedOnTime = int(i.split(':')[0])
if turnedOnTime<18 and turnedOnTime>7:
	os.system('hsetroot -cover ~/.Pictures/Wallpapers/Astronaut-butterfly.jpg')
else:
	os.system('hsetroot -cover ~/.Pictures/Wallpapers/Burning-austonaut.jpg')

