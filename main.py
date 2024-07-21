import subprocess
import os
import get_pip
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    print("[GAME] Trying to import pygame")
    import pygame
except:
    print("[EXCEPTION] Pygame not installed")

    try:
        print("[GAME] Trying to install pygame via pip")
        import pip
        install("pygame")
        print("[GAME] Pygame has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")
        print("[GAME] Trying to install pip")
        get_pip.main()
        print("[GAME] Pip has been installed")
        try:
            print("[GAME] Trying to install pygame")
            import pip
            install("pygame")
            print("[GAME] Pygame has been installed")
        except:
            print("[ERROR 1] Pygame could not be installed")

import courses
import physics
import startScreen
import sys
import math
from time import sleep, time
import tkinter as tk
from tkinter import messagebox

pygame.init()

SOUND = False

winwidth = 1080
winheight = 600
pygame.display.set_caption("Super Minigolf")

def load_image(file_path):
    '''
    helper func to load image and handle errors
    '''
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Error loading image {file_path}: {e}")
        return None


icon = load_image(os.path.join('img', 'icon.ico'))
icon = pygame.transform.scale(icon, (32,32))
background = load_image(os.path.join('img', 'back.png'))
sand = load_image(os.path.join('img', 'sand.png'))
edge = load_image(os.path.join('img', 'sandEdge.png'))
bottom = load_image(os.path.join('img', 'sandBottom.png'))
green = load_image(os.path.join('img', 'green.png'))
flag = load_image(os.path.join('img', 'flag.png'))
water = load_image(os.path.join('img', 'water.png'))
laser = load_image(os.path.join('img', 'laser.png'))
sticky = load_image(os.path.join('img', 'sticky.png'))
coinPics =  [
    load_image(os.path.join('img', 'coin1.png')),
    load_image(os.path.join('img', 'coin2.png')),
    load_image(os.path.join('img', 'coin3.png')),
    load_image(os.path.join('img', 'coin4.png')),
    load_image(os.path.join('img', 'coin5.png')),
    load_image(os.path.join('img', 'coin6.png')),
    load_image(os.path.join('img', 'coin7.png')),
    load_image(os.path.join('img', 'coin8.png'))
    ]
powerMeter = load_image(os.path.join('img', 'power.png'))
powerMeter = pygame.transform.scale(powerMeter, (150,150))

pygame.display.set_icon(icon)

coinTime = 0
coinIndex = 0
time = 0
rollVel = 0
strokes = 0
par = 0
level = 8
flagx = 0
coins = 0
shootPos = ()
ballColor = (255,255,255)
ballStationary = ()
line = None
power = 0
hole = ()
objects = []
put = False
shoot = False
start = True

if SOUND:
    wrong = pygame.mixer.Sound(os.path.join('sounds', 'wrong12.wav'))
    puttSound = pygame.mixer.Sound(os.path.join('sounds', 'putt.wav'))
    inHole = pygame.mixer.Sound(os.path.join('sounds', 'inHole.wav'))
    song = pygame.mixer.music.load(os.path.join('sounds', 'music.mp3'))
    splash = pygame.mixer.Sound(os.path.join('sounds', 'splash.wav'))
    pygame.mixer.music.play(-1)

# POWER UP VARS
powerUps = 7
hazard = False
stickyPower = False
mullagain = False
superPower = False
powerUpButtons = [[900, 35, 20, 'P', (255,69,0)],[1000, 35, 20, 'S', (255,0,255)], [950, 35, 20, 'M', (105,105,105)]]

# Fonts
myFont = pygame.font.SysFont('comicsansms', 50)
parFont = pygame.font.SysFont('comicsansms', 30)

win = pygame.display.set_mode((winwidth, winheight))

class scoreSheet():
    def __init__(self, parr):
        self.parList = parr
        self.par = sum(self.parList)
        self.holes = 9
        self.finalScore = None
        self.parScore = 0
        self.strokes = []
        self.win = win
        self.winwidth = winwidth
        self.winheight = winheight
        self.width = 400
        self.height = 510
        self.font = pygame.font.SysFont('comicsansms', 22)
        self.bigFont = pygame.font.SysFont('comicsansms', 30)


    def getScore(self):
        return sum(self.strokes) - sum(self.parList[:len(self.strokes)])
    
    def getPar(self):
        pass