#By: Archie, Final Project, December 5th, 2017 - January 8th, 2018.

#Read this first :)
#This was my first ever project I did in grade 10. Also sorry if the programming is just a little bit messy or hard to understand
#Also, when putting in information into the program, I would suggest copying the text inside the quotations and also using 1000 in the line thickness for a better picture
#Also also, the "goto", "forward","line" , "space" , "rectangle" and "turn" are boring 

#imports time, turtle, and random
import time
import turtle
import random

#makes a shortcut, sets turtle.Turtle() equal to just "t."
t=turtle.Turtle()

#sets the speed of the program equal to zero, which is the fastest speed possible
t.speed(0)

#the colour black makes it easier for the user to see his art
turtle.bgcolor("black")

#makes  a list of colors, these will be used later in the program
colors=["white"]

#displays instructions
print(
"""Intructions:
To make a drawing using lines, shapes, colors, just type in the name of that certain shape and then follow the programed instructions.""")
#pauses the program so the user has time to read the instructions
#time.sleep(7)
print(
"""The options are:

1.) Selecting coordinates to start : "goto"
2.) Moving forward: "forward" or "line"
3.) To turn: "turn"
 4.) Leave empty space: "space"
5.) Draw a rectangle: "rectangle"
6.) Draw Squares or Squares' Patterns: "S pattern"
7.) Draw a circle or Circles' patterns: "C pattern"
8.) Draw a Polygon: "polygon"
9.) Stars patterns: "star"
10.) To make random patterns: "patterns"
11.) To end program: "end program".""")
print
("Functions 1 and 4 are very similar, but can be used differently and may be more useful depending on the function.")
#pauses the program so the user has time to read the instructions
#time.sleep(20)

print(
"""
Color Choices are: "gold", "purple", "red", "yellow", "blue", "pink", "black", "orange", "green", "magenta", "white", "brown"
PLEASE ENTER ONLY WHOLE NUMBERS, NO Decimals,Also try using odd numbers for a more interesting image""")
#pauses the program so the user has time to read the instructions
#time.sleep(5)
print(
"""
HAVE FUN DRAWING!!!
""")

#declare variable

lineWidth=0
start=0
length=0
width=0
degR=0
degL=0
controlnum=0
widthNum=0
numberOfSides=0
sideLength=0
angle=0
turn=0
sizeInc=0
size=0
repeat=0
x=0
y=0
cChoice=0
deg=0
big=0

#declare function

#defines function 'goTo' and sets x and y as the parameters
def goTo(x,y):
        #turtle picks up the pen, so when starts travelling to the coordinates given, it doesn't make a line from the originals spot to that specific coordinate.
        t.penup()
        #goes to that certain coordinate, based on the arguments given
        t.goto(x,y)
        #turtle puts the pen down, so now you can start drawing
        t.pendown()
        return

#defines fucntion 'space', sets length as the only parameter
def space(length):
        #picks pen up
        t.penup()
        #moves to the location(it's a lot like the goTo function, it basically is just another option for moving without leaving a mark).
        t.forward(length)
        #puts pen down
        t.pendown()

#defines fucntion 'forward' and sets length as the only parameter
def forward(length):
        #asks the user to choose a color, from the list provided at the beginning.
        color_Choice=str(input("what color would like to use?"))
        t.color(color_Choice)
        #moves forward according to the length input
        t.forward(length)
        return

#defines fucntion 'rectangle', sets lenght and width as the parameters
def rectangle(length, width):
        #allows the user to select the color
        color_Choice=str(input("what color would like to use?"))
        t.color(color_Choice)
        #starts filling in the shape with the color selected
        t.fillcolor(color_Choice)
        t.begin_fill()
        #repeats the followwing function twice.
        for i in range(2):
        #moves forward the desired length
            t.forward(length)
        #turns left 90 degrees
            t.left(90)
        #makes the width the desired length
            t.forward(width)
        #turns 90 degrees left
            t.left(90)
        #ends the filling of the color when the rectangle is finished
        t.end_fill()
            

#defines fucntion 'squarepattern', sets length, repeat, and big as it's parameters,      
def squarePattern(length, repeat, big):
        #while cChoice(a variable used later in the program) is 'yes', runs the following program
        while cChoice!="yes":
                #repeats it the number of times the user selected it to repeat
                for i in range(repeat):
                        #randomly chooses a color from the list of color provided earlier
                        t.color(random.choice(colors))
                        #moves forward the selected length
                        t.forward(length)
                        #turns left 90 degrees
                        t.left(90)
                        #moves forward the selected length
                        t.forward(length)
                        #turns left 990 degrees
                        t.left(90)
                        #moves forward the selected length
                        t.forward(length)
                        #turns left 90 degrees
                        t.left(90)
                        #moves forward the selected length
                        t.forward(length)
                        #redefines length and adds variable 'big' to it each time, so it increases in size each time the program loops(big is selected by the user, meaning they select how much it increases in size each time it loops.).
                        length+=(big)
                        #turns left the selected length
                        t.left(big)
                        
        #in case the first part isn't wanted, this is used in place of that.                
        else:
        #repeats it the selected number of times
            for i in range(repeat):
                    #randomly chooses a color
                    t.color(random.choice(colors))
                    #starts filling in the shape with a randomly chosen color
                    t.fillcolor(random.choice(colors))
                    t.begin_fill()
                    #moves forward
                    t.forward(length)
                    #turns left 90 degrees
                    t.left(90)
                    #moves forward
                    t.forward(length)
                    #turns left 90 degrees
                    t.left(90)
                    #moves forward
                    t.forward(length)
                    #turns left 90 degrees
                    t.left(90)
                    #moves forward
                    t.forward(length)
                    #ends the filling of the shape
                    t.end_fill()
                    #redefines length and adds variable 'big' to it each time, so it increases in size each time the program loops(big is selected by the user, meaning they select how much it increases in size each time it loops.).
                    length+=(big)
                    #turns left
                    t.left(big)
                    

        

#defines function 'circlePattern', sets radius, turn, repeat, and big as the parameters        
def circlePattern(radius, turn, repeat, big):
        #while cChoice isn't 'yes', run the following program
        while cChoice != "yes":
                #repeat the selected number of times
                for i in range(repeat):
                        #randomly selects a color
                        t.color(random.choice(colors))
                        #makes the radius of the circle the selected length
                        t.circle(radius)
                        #redefines radius and adds variable 'big' to it each time, so it increases in size each time the program loops(big is selected by the user, meaning they select how much it increases in size each time it loops.).
                        radius+=big
                        #turns left the selected angle
                        t.left(turn)
        #in case the first part isn't wanted, this is used in place of that.
        else:
            #repeat the selected number of times
            for i in range(repeat):
                    #randomly selects a colors
                    t.color(random.choice(colors))
                    #starts fillng in the shape
                    t.fillcolor(random.choice(colors))
                    t.begin_fill()
                    #makes the circles' radius the desired length
                    t.circle(radius)
                    #redefines radius and adds variable 'big' to it each time, so it increases in size each time the program loops(big is selected by the user, meaning they select how much it increases in size each time it loops.).
                    radius+=big
                    #turns left the desired length
                    t.left(turn)
                    #ends the filling of color
                    t.end_fill()

                    
#defines function 'star', sets size and angle as the parameters
def star(size, angle):
        #repeat the selected number of times
        for i in range(repeat):
                #redines size and the size will increase depending on the increasing size(sizeInc)
                size+=sizeInc
                #randomly selects a color
                t.color(random.choice(colors))
                #starts to fill the star with a randomly selected color
                t.fillcolor(random.choice(colors))
                t.begin_fill()
                #sets count equal to zero
                count = 0
                #turns right
                t.right(turn)
                #while count is less than 5
                while count <=5:
                        #move forward
                        t.forward(size)
                        #turn right
                        t.right(angle)
                        #add one to count
                        count+=1
                        #ends the filling of color
                        t.end_fill()


#defines function 'turn', sets no parameters(I was just experiementing to see if the fucntion would work without any parameters, and... IT DID!!!).
def turn():
        #turns right depending on the degrees' input by the user
        t.right(degR)
        #turns left depending on the degress' input by the user(turns left and right because I wanted to keep it short and not make 2 different functions for the same need,(IT WAS MORE EFFIECIENT TO DO IT LIKE THIS)).
        t.left(degL)
        return


#defines fucntion 'polygonPattern', sets parameters
def polygonPattern(repeat, numberOfSides, sideLength,angle, sizeInc):
        #repeat the selected number of times
        for i in range(repeat):
                #turn right
                t.right(turn)
                #repeats based on the number of sides the user wants to have
                for i in range(numberOfSides):
                        #randomly selects a color
                        t.color(random.choice(colors))
                        #moves forward
                        t.forward(sideLength)
                        #turn right
                        t.right(angle)
                        #redefines sideLength and adds sizeInc to it each time the fucntion loops
                        sideLength+=sizeInc



print("WELCOME TO DRAWING WITH EASE! Follow the instructions provided and you'll be a master in no time!")#this line welcomes the user      
lineWidth=int(input("please input the line thickness you'd like to use.(thickest = 1000, thinnest = 1)"))#asks for the width of the line that the user will be drawing with
start= str(input("what would you like to draw first? "))#aks what they would like to draw first 
t.width(lineWidth)#takes the number that the user inputed and puts it into the program
while start != "end":#begans the loop and if the user inputs 
    if "space" in start:#the first option 
        length=int(input("how much empty space would you like to leave?"))#asks for the length of the space 
        space(length)#creates the space 

    if "turn" in start:#the second option 
        degR=int(input("How many degress would you like turn right?"))#turns the user with the amount of degrees that the user wanted 
        degL=int(input("How many degress would you like to turn left?"))#turns the user with the amount of degrees that the user wanted
        turn()#turns the user to which ever direction they wanted to be turned 
        start=str(input("What would you like to draw next?"))#asks what they would like to draw next 

    if "forward" in start:#the third option
        length=int(input("How far would you like to move forward?"))#asks the user for the length of there line 
        forward(length)#moves the user forward by the length the wanted to go  
        start=str(input("What would you like to draw next?"))#asks what they would like to draw next
            

    if "rectangle" in start:#the fourth option
        length=int(input("Please enter the length of the rectangle"))#asks the user for the length of the rectangle 
        width=int(input("Please enter the width of the rectangle"))#asks the user for the width of the reactangle 
        rectangle(length, width)#sends the information to the function and makes the reactangle 
        start=str(input("What would you like to draw next?"))#asks what they would like to draw next


    if "S pattern" in start:#the fifth option
            cChoice=str(input("would you like to fill in shapes with colors"))#asks if the user wants to fill the space in the squares in the pattern 
            length=int(input("what would you like the side length to be?"))#asks the user for how big the squares should be 
            repeat=int(input("how many times would you like the pattern to repeat?"))#asks the user how many times should the pattern repeat 
            deg=int(input("how many degrees would you like pattern to turn, each repetition?"))#asks the user how close or far should the squares of the pattern be 
            big=int(input("How much would you like the squares to increase in size each repetition?"))#finally asks the user how the squares should increse in size 
            squarePattern(length, repeat, big)#sends the info to the function and starts the pattern 
            print("Thank you for using our program. If you would like to try again please close the program and run it again")#this line tells the user that if they want to try again and draw something else they have to restart the program 
            break#this stops the form continuing the loop
                        

    if "C pattern" in  start:#the sixth option
            cChoice=str(input("would you like to fill in shapes with colors"))#asks if the user wants to fill the space in the circles in the pattern
            radius=int(input("what radius would you like the circular pattern to be?"))#asks the user for how big the circles should be
            repeat=int(input("how many times would you like the pattern to repeat?"))#asks the user how many times should the pattern repeat
            turn=int(input("How many degrees would you like the circle to turn, each repetition?"))#asks the user by by how many degrees far apart the circles should be 
            big=int(input("How much would you like the circles to increase in size each repetition?"))#asks the user how big the circles should get in every repetition 
            circlePattern(radius, turn, repeat, big)#sends the info to the function and starts the pattern 
            print("Thank you for using our program. If you would like to try again please close the program and run it again")#this line tells the user that if they want to try again and draw something else they have to restart the program
            break#this stops the form continuing the loop

    if "patterns" in start:#the seventh option
            controlNum=int(input("Please Enter a number: \n(The best number to try are 30,45,60,62,67,70,71,87,89,90,91,97,100,144,145,150)\n"))
            widthNum=int(input("Please Enter a number for the width of the line: \n(The best numbers to try are 1 to 1000)"))
            circleQues=str(input("Would you like to draw with circles or with lines?(Line/Circle)"))#asks the user if they want to draw with lines or circles 
            circleQues=circleQues.lower()#lowers the user's answer
            t.penup()#this lifts the pen up so drawing no occurs 
            t.goto(0,0)#this puts the pen in the center 
            t.pendown()#this puts the pen down so the drawing can resume
            for x in range (500): #This controls how many times the program loop  
                t.color(random.choice(colors))#this line picks form a list of colours randomly 
                if circleQues == ("circle"):#if the user picks circles the lines below star to happens  
                    t.width(x/widthNum+1)#This controls the width of the drawing 
                    t.circle(x)#this draws the circles with the 'x' being width of the circles 
                    t.left(controlNum)#this controls where the circles should be drawen 
                else:#if the user picks lines the lines below star to happens  
                    t.width(x/widthNum+1)#This controls the width of the drawing 
                    t.forward(x)#this draws the lines with the 'x' being width of the lines
                    t.left(controlNum)#this controls where the lines should be drawen 

            print("Thank you for using our program. If you would like to try again please close the program and run it again")#this line tells the user that if they want to try again and draw something else they have to restart the program
            break#this stops the form continuing the loop

    if "polygon" in start:#the eighth option
            numberOfSides=int(input("please enter the number of sides you'd like your polygon to have."))#asks the user for the number of sides that there shape should have 
            sideLength=int(input("please enter the side length of each of the sides"))#asks the user for the lengths of the sides of there shape 
            angle=360/numberOfSides#this divides the number that the user entered by 360 so the shape is closed and is properly proportion
            repeat=int(input("how many times would you like your polygon to repeat the pattern?"))#this asks how many times the shape should be repeated 
            turn=int(input("how many degress would you like your polygon to rotate each repetition(rotate to the right)?"))#this lines asks how many degrees they would like there shape to be moved by
            sizeInc=int(input("how much would you like the polygons to increase in size, each repetition?"))#this lines asks how big there shape should be with each repetition 
            polygonPattern(repeat, numberOfSides, sideLength,angle, sizeInc)#this line sends the info to the funtion 
            print("Thank you for using our program. If you would like to try again please close the program and run it again")#this line tells the user that if they want to try again and draw something else they have to restart the program
            break#this stops the form continuing the loop
            
    if "star" in start:#the nineth option
        size=int(input("please input the side length for the star."))#this line asks for the size of the star 
        angle=144#this is the angle that makes a star
        repeat=int(input("how many times would you like to repeat the star pattern?"))#it asks how many times the user want like the star to be repeated 
        turn=int(input("how many degrees would you like your star to turn each repetition?"))#it asks the user how much space should be in the pattern 
        sizeInc=int(input("how much would you like the star to increase in size, each repetition?"))#this asks how big the star should get after each repetition 
        star(size, angle)#this sends the info to the function and executes the function 
        print("Thank you for using our program. If you would like to try again please close the program and run it again")#this line tells the user that if they want to try again and draw something else they have to restart the program
        break#this stops the form continuing the loop
        

    if "goto" in start:#the tenth option
            x=int(input("please input the x coordinate"))#asks the user which x coordinate they would like to go to 
            y=int(input("please input the y coordinate"))#asks the user which y coordinate they would like to go to
            goTo(x,y)#sends the input to the function and puts the user at the x and y coordinate they wanted to go to 
            start=str(input("what would you like to draw next?"))#asks what they would like to draw next

    if "end" in start:#the final option that ends the program 
            break#this stops the form continuing the loop
    else:
        print("please check your spelling and try again")#this line comes up when the user inputs something wrong 
        start=str(input("what would you like to draw next?"))#asks what they would like to draw next
