###################################################################
#FILE: HelloTurtle.py                                             #
#WRITER: Ran Shaham,ransha,203781000                              #
#EXERCISE: intro2cs ex1 2014-2015                                 #
#DESCRIPTION:                                                     #
#A program that draws some simple geometric shapes on the screen  #
#and prints "Hello Turtle!", using Turtle graphics.               #
###################################################################
import turtle

#title for the display window
turtle.title("Fun with Tutrtle Graphics and Python")
turtle.up()            #lift the pen up, no drawing.
turtle.goto(-100,-100) #move turtle to the absolute position (-100,-100)
turtle.down()          #pen is down, drawing now.
# I will now draw a red square.
turtle.color("red")
turtle.goto(100,-100)  #moves the pen 200 points ONLY to the right,
                       #thus creating the lower end of the square.
turtle.goto(100,100)   #the right end of the square (200 points ONLY on the y axis) and so on...
turtle.goto(-100,100)
turtle.goto(-100,-100) #returned to the initial point.
#Now for an orange circle. since the circle's center in Turtle is drawn 'r'
#points to the LEFT of the turtle's position, and the turtle is heading
#to the east, I will start drawing from the point (0,-100) because the
#circle radius is 100 (and this point is 100 points to the RIGHT of turtle,
#so the center will be at (0,0))
turtle.up()
turtle.goto(0,-100) 
turtle.down()
turtle.color("orange")
turtle.circle(100)
#Now for the bigger blue square. I actually guessed the first 2 coordinates
#of the new square because it looked reasonable, but after it worked I understood why my guess makes sense.
turtle.up()
turtle.goto(-200,0)
turtle.down()
turtle.color("blue")
turtle.goto(0,-200)
turtle.goto(200,0)
turtle.goto(0,200)
turtle.goto(-200,0)
#Now for the writing command (which is given in the instructions...)
turtle.up()
turtle.goto(-70,-5)
turtle.down()
turtle.color("green")
turtle.write("Hello Turtle!", font=("Arial", 20, "normal"))
#done
turtle.done()
