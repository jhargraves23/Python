from graphics import *


    
win = GraphWin("Jacob's Bagels App",500,500)
win.setCoords (0.0,0.0,6.0,6.0)
win.setBackground('Sky Blue')

#Bagel
center = Point(2,1.0)
bagelCircle = Circle(center,.5)
bagelCircle.setFill('tan')
bagelCircle.draw(win)

aLine = Line(Point(1.5,1),Point(2.5,1))
aLine.draw(win)

center = Point(2,1.0)
bagelCircle = Circle(center,.08)
bagelCircle.setFill('black')
bagelCircle.draw(win)


#User Input statement
Text(Point(1,5.5), "Enter Your Name: ").draw(win)
Text(Point(3,5.8), "Welcome to Bonnie's Best Bagels App").draw(win)
Text(Point(1.5,5), "Enter the amount of Bagels of your preference").draw(win)      
Text(Point(1,4.7), "Bagels:").draw(win)
Text(Point(2,4.6), "Everything").draw(win)
Text(Point(2,4.0), "Plain").draw(win)
Text(Point(2,4.3), "Multigrain").draw(win)
Text(Point(1,3.6), "Toppings:").draw(win)
Text(Point(2,3.6), "   Cream Cheese   $.50").draw(win)
Text(Point(2,3.3), "   Butter  $.25").draw(win)
Text(Point(1,2.9), "Coffee: ").draw(win)
Text(Point(2,2.8), "Regular Coffee $1.95").draw(win)
Text(Point(2,2.5), "Decaf Coffee $1.85").draw(win)



#create interface

inputName = Entry(Point(4.5,5.5),9)
inputName.setText("-")
inputName.draw(win)
inputEverythingB = Entry(Point(4.5,4.6),5)
inputEverythingB.setText("0")
inputEverythingB.draw(win)
inputMultiB = Entry(Point(4.5,4.3),5)
inputMultiB.setText("0")
inputMultiB.draw(win)
inputPlainB = Entry(Point(4.5,4.0),5)
inputPlainB.setText("0")
inputPlainB.draw(win)

inputCC = Entry(Point(4.5,3.6),5)
inputCC.setText("0")
inputCC.draw(win)
inputButter = Entry(Point(4.5,3.3),5)
inputButter.setText("0")
inputButter.draw(win)

inputRC = Entry(Point(4.5,2.9),5)
inputRC.setText("0")
inputRC.draw(win)
inputDC = Entry(Point(4.5,2.5),5)
inputDC.setText("0")
inputDC.draw(win)



outputTotal = Text(Point(4.5,1.8),6)
outputTotal.setText("0")
outputTotal.draw(win)

button = Text(Point(1.6,1.7), "Calculate Total")
button.draw(win)
Rectangle(Point(1,1.5), Point(2.5,2)).draw(win)

win.getMouse()


EverythingB = float(inputEverythingB.getText())
MultiB = float(inputMultiB.getText())
PlainB = float(inputPlainB.getText())
CC = float(inputCC.getText())
Butter = float(inputButter.getText())
RC = float(inputRC.getText())
DC = float(inputDC.getText())
#equation for input
total = ((1.75 * EverythingB) + (1.75 * MultiB) + (1.75 * PlainB) + (0.50 * CC) + (0.25 * Butter) + (1.95 * RC) + (1.85 * DC) *.07)

outputTotal.setText(total)

center = Point(100,100)

yellowCircle = Circle(center,30)
yellowCircle.setFill('yellow')
yellowCircle.draw(win)

win.getMouse()
win.close()


