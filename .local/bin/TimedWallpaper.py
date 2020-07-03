#/usr/bin/python3

import subprocess, random, os, time
imageList = subprocess.getoutput("ls ~/.Pictures/Wallpapers").split('\n')
imageListLen = len(imageList)-1

for i in time.asctime().split(' '):
	if ':' in i:
		turnedOnTime = int(i.split(':')[0])
if turnedOnTime<18 and turnedOnTime>7:
	os.system('hsetroot -cover ~/Pictures/Wallpapers/Astronaut-butterfly.jpg')
else:
	os.system('hsetroot -cover ~/Pictures/Wallpapers/Burning-austonaut.jpg')

