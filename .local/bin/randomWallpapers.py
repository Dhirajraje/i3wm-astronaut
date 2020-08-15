#!/usr/bin/python3
import random, subprocess, os, sys

path="~/.Pictures/Wallpapers/"
images=subprocess.getoutput("ls ~/.Pictures/Wallpapers/").split('\n')
os.system(f"hsetroot -cover ~/.Pictures/Wallpapers/{random.choice(images)}")

	
