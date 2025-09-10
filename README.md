# PyAr4

A Python library to control the AR4 robotic arm. 

This Library provides fast to implement controlls of the AR4 robotic arm for automation, education and research. For rapid development and prototyping both real-world and simulated backends are supported. For custom backends see below.

## Installation and quick start
```bash
pip install -e . 
```

To start create a Robot object. 
```python
from pyar4 import Ar4

robot = Ar4()
robot.calibrate()
```
Before any action can be taken, the arm has to be calibrated. This is to ensure the correct position after the startup


You can both move the arm directly to a given position, move an individual joint or schedule a predefined command of your backend.
```python
robot.move(x=10, y=20, z=-5)
robot.gripper.close()
robot.moveJoint(id=5, deg=20)
robot.gripper.open()

instruction = robotInstruction({'cmd':'moveJ', 'id':2, 'deg':15})
robot.scheduler(instruction)
```

If you need to reuse a position multiple times, it is enough to navigate there once - save it and then load it as needed.
```python
robot.move(x=10, y=20, z=-5)
robot.savePosition(name='home')

robot.move(x=0, y=20, z=-5)
robot.gripper.close()
robot.movePosition(name='home')
```

## Features
- Logging

## Commands
startup() :  safe start of the robot, has to be called after a shutdown.

# Safety / Control
def stop() : stops current movements and cleares potential scheduled moves

def shutdown() : stronger than stop(), sends abort to current movement, halts instantly

def calibrate() : calibrate joints and move to home position.

# Movement
def move_to(x: float, y: float, z: float, orientation: list[float] = None) : Move to a given kartesian
    coordinate, optionally the orientation can be specified

def move_joint(idx: int, val: float) : move a single joint by a given amount of degrees

def set_joint_angles(angles: list[float]) : move multiple joints at once, if supported by backend. 
    Otherwise wrapper for move_joint

def set_home() : set a new home position

def home() : move to home position

def save_position(name: str, *args) : save position under a given name

def move_to_position(, name: str) : if position with given name exists move to it

# Motion Planning
def execute_trajectory(angles: list[list[float]]) : list of joint angles, that get are moved to one after
    another. wrapper around set joint angles, after one position is reached
    continue to the next in the list.

# Gripper
def open_gripper() : opens the gripper

def close_gripper() : closes the gripper

# State / Sensoring
def get_joint_angles() : return a list of the current joint angles

def get_position() : returns a list containing both the coordinates and orientation of the gripper

# To add
def offset_coords(int x, int y, int z, phi1, phi2, phi3) : offset in cartesian frame

## Predefined Commands by the interface
# coordinate system
these are clear
xVal
yVal
zVal 
rzVal
ryVal
rxVal

what does this mean? - it is also somehow seperate from all the other coordinates
trVal

# Parameters
Known:

Unknown:
    -LoopMode = str(J1OpenLoopStat.get())+str(J2OpenLoopStat.get())+str(J3OpenLoopStat.get())+str(J4OpenLoopStat.get())+str(J5OpenLoopStat.get())+str(J6OpenLoopStat.get())
    -speedPrefix
    -Speed
    -ACCspd
    -DECspd
    -ACCramp
    -WC

# Use ser connection
Known what they do:
    -connect teensy 
    -connect arduino 
    -Wait time 
    -Tool S
    -Move J
    -OFFS J
    -Move A 
    -Move C 
    -Move L

Not known what exactly they do:
    -Calibrate (Where is the code for that?)
    -test limit switch 
    -Wait 5v IO board 
    -Set Output 5v IO Board

Not known what they do:
    -set enc 
    -read enc 
    -servo_cmd 
    -If Input 
    -If Modbus Coil 
    -If Modbus Input 
    -If Modbus Holding Register 
    -If Modbus Input Register 
    -Wait Modbus Coil 
    -Wait Modbus Input 
    -Set Modbus Coil 
    -Set Modbus Register 
    -Start spline
    -End spline
    -Move Vis 
    -Move PR 
    -OFFS PR 
    -Move R 

# Do not use ser connection
call program -
executeRow -
Run Gcode Program -
Return Program -
Jump to Row -
# unsure wether or not
Read Com ? servo3?
If Register ? what does eval do?
If COM device ?
Set Register ?
set postion register ?
Camera on ? 
Camera off ?
Vision Find ?

# in doc but not yet found in the code
move sp
teach sp
off sp

# additional doc to read
c. IO
- The set output on or set output off buttons allow you to insert a
line of code that will turn Arduino IO of your choice on or off (see
bottom on input outputs tab for available IO pins on the Arduino
Mega). For example, if you have a pneumatic gripper you would
hook up your solenoid per the wiring harness manual to output
Arduino pin #38 and ender a line of code "Out On = 38" to
control your gripper.
d. Navigation
You can create as many program routines as you like. Enter the
name of the program you would like to create in the program field
and press "load program", if the program does not already exist it
will be created, if you have already created a program of that name
it will be loaded. Programs are created in your software folder and
can be deleted from that file location if no longer needed.
- The "Call Program" button allows you to insert a line of code that
calls a program.
- The "Return" button inserts a line of code that will allow the
called program to return to the program it came from. *note you
cannot call another program from within a program that has already
been called, you must return to the main program before calling
another program. For example, you will likely want to create a
program called "Main" from that program you might call a program
called "Pickup Part" at the end of pickup part you will want to
insert a "Return" line to get back to the "Main" program, then you
can do other things or call other programs. You cannot call another
program from "Pickup Part" you must first return to the main
program.
- the "Create Tab" button allows you to create markers in your
program that you can jump or navigate to based on conditions.
*note you cannot have 2 tabs with the same number - each tab
needs a new number. This functionality is very similar to basic
programming.
- The "Jump to Tab" button allows you to jump to a tab, for example
you could put "Tab 1" at the top of your program and at the
bottom put a "Jump to Tab 1" and then your program would loop
indefinitely.
The "If Register Jump" button allows you to jump to a tab based on
the condition of a register. For example you could have a looping
program as previously described but then add a line into your
program that increments a register and then add a line prior to
"Jump to Tab 1" that says "If Register 1 = 5 Jump to Tab 2" and then
place a "Tab 2" at the very bottom after "Jump to Tab 1" so that the
program will run 5 times and then jump to Tab 2 and stop.
e. Registers
The "Register" button allows you to set a register to a static value
or you can add a "++" before the number and the register will then
be incremented by the amount. For example, if you just enter a "1"
it will always set that register to a value of 1 but if you enter "++1"
it will then increment that register by 1 every time the line is run
so that you can use this for counting. You can enter any number, for
example you could enter "++3" and count by 3's if you like. The
same is true for counting down or decrementing - just place a "--"
before the number.
f. Servos
The Servo button allows you to control external servos - it’s not
for the robot itself, it’s for use if you have a servo gripper or a
servo actuator that you want the robot program to control. For
example, if you had a servo gripper that you had hooked up to
Arduino pin A0 per the wiring harness manual you could then
insert a line of code "Servo number 0 to position: 180" to open the
gripper and "Servo number 0 to position: 0" to close your gripper.
g. Editing lines of code
You can select a line of code in you command window and then
press the "get selected" button, this will copy that line into the
manual entry field. You can now edit the line of code in the manual
entry field, some examples might be: changing the stored position
number, changing a position, changing the robot speed or
acceleration. Now with your edited line of code you can reselect
the original line of code in your command window and then press
the "replace" button and the old line of code will be replaced with
the new edited line. The "insert" button will insert the test from
the manual entry field into your program without replacing - you
can use this to insert comments or hand written lines of code using
the insert button, this can be used to copy a line of code from the
program and then paste or insert in in numerous places in the
program.
4. CALIBRATION
a. Auto Calibration
Pressing the auto calibration button will auto calibrate all axis. The
robot will run to its full limit in the default directions and set each of
the joint values accordingly. You can also use the individual buttons
to calibrate each axis one at a time.
b. Force to midrange Calibration
This button allows you to force each axis to be calibrated at its mid-
point. This is only used when setting up your robot - for example if
your robot is not yet calibrated and you are trying to jog a joint
around and you hit an axis limit this button will allow you to do
what you need to do before you can auto calibrate your robot.
Only use this button during construction and setup.

## Todo: 
Now:
- response handler
- think about robot commands, what do we want to support?
    - define features in version 1.0
    - inverse kinematics - is it necessary?
    - clean up base ar4 class
- rewrite base class controller, what is actually necessary?
- add all functions from the ui to servo backend
    - how do they all work
    - check what parameters do?
- how can we controll the gripper?

- Instructions via dictionary?


Future:
- command dataclass, queue, scheduler.  How should this work?
- safety monitor, can we do this? What should it support?
- simulation backend? which simulation software to support?
- change backend parameters
- add tool frame
    - support for any reference frame?

## Features version 1.0:



