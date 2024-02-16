# imports
from psychopy import visual, core, prefs
import numpy as np
import serial

# set PTB as audio backend, force low latency 
# (change to "0" in case of trouble)
prefs.hardware['audioLib'] = ['PTB']
prefs.hardware['audioLatencyMode'] = 3

# this needs to be imported AFTER setting the audio backend
from psychopy import sound


# CONFIG

# address of the serial port, OS dependent
# more info on setting this here: https://workshops.psychopy.org/3days/day3/hardware/index.html
serial_port_address = '/dev/tty.usbserial-D30C1INU'

# serial port baudrate (this is given by the BioSemi trigger interface spec)
baudrate = 115200

# serial port spec
# comment out if not using serial port
port = serial.Serial(serial_port_address, baudrate)

# how many sounds to play
d = 30     


# define PsychoPy window
win = visual.Window([400,400]) 

# define sounds
std = sound.Sound(500, .2)
dev = sound.Sound(800, .2)

# flip screen
win.flip()
    
    
sound_list = list(range(d))    

# for every sound...    
for i in sound_list:
    next_flip = win.getFutureFlipTime(clock='ptb')

    # if deviant...
    if np.random.uniform() < .2:
        dev.play(when=next_flip)
        win.callOnFlip(port.write, str.encode('2'))
    
    # if standard...
    else:
        std.play(when=next_flip)
        win.callOnFlip(port.write, str.encode('1'))
    
    win.flip()
    win.callOnFlip(port.write, str.encode('0'))
    
    for _ in range(59):
        win.flip()


