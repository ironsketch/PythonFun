import turtle
wn = turtle.Screen()
wn.bgcolor('Black')
wn.title('Cool Stuff')
turd = turtle.Turtle()
turd.color('Light Gray')
############################################################################

def inspi(side,angle,inc):
    turd.fd(side)
    turd.rt(angle)
    inspi(side, angle + inc, inc)

inspi(10,2,20)

############################################################################

##def polyspi(side):
##    turd.fd(side)
##    turd.rt(117)
##    polyspi(side + 5)
##
##polyspi(10)

############################################################################

##def thing():
##    for i in range (2):
##        turd.fd(100)
##        turd.rt(90)
##    for i in range (2):
##        turd.fd(50)
##        turd.rt(90)
##    turd.fd(100)
##    turd.rt(90)
##    for i in range (2):
##        turd.fd(25)
##        turd.rt(90)
##    turd.fd(50)
##
##def runThing():
##    for i in range (18):
##        thing()
##        turd.rt(10)
##        turd.fd(50)
##
##runThing()

############################################################################

##def ray():
##    for i in range (2):
##        turd.circle(120, 90)
##        turd.rt(30)
##        turd.circle(-120, 90)
##        turd.lt(200)
##
##def sun():
##    for i in range (6):
##        ray()
##        turd.rt(40)
##
##sun()

############################################################################

##def petalSize():
##    for i in range (2):
##        turd.circle(120, 60)
##        turd.lt(120)
##    
##def main():
##    # Main SHTUFF
##    for i in range (6):
##        petalSize()
##        turd.rt(60)
##
##main()
