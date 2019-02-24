import serial

port="/dev/ttyUSB0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

def alarm():
    variable = int(serialFromArduino.readline())
    
    return variable

"""

import serial
import environment

port="/dev/ttyUSB0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

beacon = []

def alarm():
    input_s = serialFromArduino.readline()
    ipt = int(input_s)
    print "sensor: "+str(ipt)

    if ipt == 1:
        fire = environment.witch()
    else:
        fire = 0

    return fire
"""
"""

def alarm():
    while True:
        input_s = serialFromArduino.readline()
        ipt = int(input_s)
        print "fire : "+str(ipt)

        if ipt == 1:
            fire = environment.witch()
        else:
            fire = 0

        return fire
"""


"""
def alarm():
    beacon = []
    while True:
        input_s = serialFromArduino.readline()
        ipt = int(input_s)
        print ipt
        
        if ipt == 1:
            fire = environment.witch()
        else:
            fire = 0
        return fire
"""        

"""


import serial
import environment

port="/dev/ttyUSB0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()


def fire():
    beacon = []
    while True:
        input_s = serialFromArduino.readline()
        input = int(input_s)
        
        if input == 1:
            node = environment.witch()
            print node
            
            fire = 8
        else:
            fire = 0

        return fire
"""
