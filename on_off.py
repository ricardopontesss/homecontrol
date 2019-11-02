#by Ricardo Silva Pontes @ 2019
#!/usr/bin/python3

import argparse, sys, time, os
import RPi.GPIO as GPIO

### CONFIGURATIONS:
#GPIO:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

### END CONFIGURATIONS

#GPIO EXAMPLE (os command = gpio readall):

#  +-----+-----+---------+------+---+-Model B1-+---+------+---------+-----+-----+
#  | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
#  +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+                                                           
#  |     |     |    3.3v |      |   |  1 || 2  |   |      | (5v)....|.....|.....|............\
#  |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |             \
#  |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | (0v)....|.....|.....|..........\   \
#  |   4 |   7 | GPIO. 7 |   IN | 0 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |           \   \
#  |     |     |      0v |      |   |  9 || 10 | 1 | ALT0 | RxD     | 16  | 15  |            \   \                                            
#  |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |             \   \            note: I use relay to connect/disconnect GND 0V,                                
#  |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |              \   \                 to never use 220V into rela, to be safe.                          
#  |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |               \   \                                            
#  |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |                \   \    ___________              (-)( LIGHT )(+)             
#  |  10 |  12 |    MOSI |   IN | 1 | 19 || 20 |   |      | 0v      |     |     |                 \  (+) [ 1CH RELAY ] (NC)         |           | 
#  |   9 |  13 |    MISO |   IN | 1 | 21 ||(22)|.0.|.OUT..|.GPIO..6.|.6...|.25..|.......\          \_(-) [ BOARD 5V  ] (COM)........|           |
#  |  11 |  14 |    SCLK |   IN | 1 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |        \..........(IN) [___________] (NO)..................[- +]220V
#  |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |                                                                
#  +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+                    (+) = 5V          (NC) = NORMALLY CLOSED "Turn ON"                                                        
#  | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |                    (-) = GND         (COM) = COMMON "Connected to"                                 
#  +-----+-----+---------+------+---+-Model B1-+---+------+---------+-----+-----+                   (IN) = 5V TRIGGER  (NO) = NORMALLY OPEN "Turn OFF"                                         
                                                                                                                              
#Control 1 vars:
var_gpio_CONTROL1=22 ##Physical number to OUT 5V, to power ON one Relay or other (example one Led Light that works with 5V turn ON).

#Define script options:
def getOptions(args=sys.argv[1:]): ##Define arguments(options for the script):
    parser = argparse.ArgumentParser(description="Controla Led  .")
    parser.add_argument("-on_CONTROL1", "--on_CONTROL1",dest='on_CONTROL1',action='store_true', help="Turn on the Control1") #Can pass 2 arguments for same action
    parser.add_argument("-off_CONTROL1", dest='off_CONTROL1',action='store_true', help="Turn off the Control1")
    options = parser.parse_args(args)
    return options

options = getOptions(sys.argv[1:])
#End Define script options

#commands for Control1:
if options.on_CONTROL1:
    GPIO.setup(var_gpio_CONTROL1, GPIO.OUT)
    print ('Turn on Control1')
    exit()
if options.off_CONTROL1:
    GPIO.setup(var_gpio_CONTROL1, GPIO.IN)
    print ('Turn off Control1')
    exit()

else:
    #print("") #If commentted will for 500 error that are redirected in apache to global ok page
    print("error - no options")
    exit()
