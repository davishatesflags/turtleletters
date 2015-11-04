import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.setpos(40, 0)
        
    elif letter == "C":
        tur.setheading(0)
        tur.pu()
        tur.fd(35)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.right(90)
        tur.circle(10,180)
        tur.pu()
        tur.setpos(40, 0)

    elif letter == "B":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.circle(8,180)
        tur.right(180)
        tur.circle(8,180)
        tur.pu()
        tur.setpos(40, 0)

        
	 
       
            ## zach
    elif letter == "D":
       
            
        tur.pu()
        tur.forward(10)
        tur.right(10)
        tur.pd()
        
        tur.right(90)
        tur.forward(100)
        tur.left(90)
        tur.circle(50,180)
        
    elif letter == "E":


        tur.pu()
        tur.forward(20)
        tur.pd()

        tur.forward(30)
        tur.right(80)
        tur.forward(20)
        tur.right(20)
        tur.forward(30)

    elif letter == "F":
        tur.pu()
        tur.forward(20)
        tur.pd()

        tur.forward(30)
        tur.right(80)
        tur.forward(20)
        tur.right(20)
	
	## Noah
	
	## Joe
	
	## Desmond
	
	## Addison
    elif letter == "M":

        tur.pendown()
        tur.right(110)
        tur.forward(40)
        tur.penup()
        tur.left(180)
        tur.forward(40)
        tur.pendown()
        tur.right(140)
        tur.forward(40)
        tur.penup()
        tur.left(140)
        tur.pendown()
        tur.fd(40)
        tur.right(140)
        tur.fd(40)
        tur.penup()
        tur.left(150)
        tur.fd(40)
        tur.pendown()

    elif letter == "N":

        tur.pendown()
        tur.right(90)
        tur.forward(40)
        tur.penup()
        tur.left(180)
        tur.forward(40)
        tur.right(150)
        tur.pendown()
        tur.forward(45)
        tur.left(150)
        tur.fd(40)
        tur.penup()
        tur.right(90)
        tur.pendown()
       
        
    elif letter == "O":
        tur.pendown()
        tur.speed(100)
        tur.circle(40, 360, 40)
        tur.penup()
        tur.left(70)
        tur.fd(80)
        tur.pendown()

        ## Brian
    elif letter == "P":
        tur.lt(90)
        tur.fd(50)
        tur.rt(90)
        tur.fd(30)
        tur.rt(90)
        tur.fd(30)
        tur.rt(90)
        tur.fd(30)
    elif letter == "Q":
        tur.lt(90)
        tur.fd(50)
        tur.rt(90)
        tur.fd(30)
        tur.rt(90)
        tur.fd(30)
        tur.rt(90)
        tur.fd(30)
        tur.lt(135)
        tur.fd(25)
    elif letter == "R":
        tur.lt(90)
        tur.fd(50)
        tur.rt(90)
        tur.fd(30)
        tur.rt(90)
        tur.fd(30)
        tur.rt(90)
        tur.fd(30)
        tur.lt(135)
        tur.fd(25)

        ## Ryan
    elif letter == "G":

        tur.pu()
        tur.forward(35)
        tur.right(90)
        tur.forward(2.5)
        tur.right(90)
        tur.pd()
        tur.circle(27,180)
        tur.left(90)
        tur.forward(30)
        tur.left(90)
        tur.forward(10)
        tur.pu()
        tur.right(90)
        tur.forward(27.5)
        tur.right(90)
        tur.forward(10)
        tur.pd()

    elif letter == "H":
        
        tur.pu()
        tur.forward(2.5)
        tur.right(90)
        tur.forward(2.5)
        tur.pd()
        tur.forward(55)
        tur.right(180)
        tur.forward(27.5)
        tur.right(90)
        tur.forward(35)
        tur.right(90)
        tur.forward(27.5)
        tur.right(181)
        tur.forward(55)
        tur.pu()
        tur.forward(2.5)
        tur.right(90)
        tur.forward(2.5)
        tur.forward(2.5)
        tur.pd()

    elif letter == "I":

        tur.pu()
        tur.forward(20)
        tur.right(90)
        tur.forward(2.5)
        tur.pd()
        tur.forward(55)
        tur.right(180)
        tur.pu()
        tur.forward(57.5)
        tur.right(90)
        tur.forward(20)
        tur.pd()
	
	## Hunter
    elif letter == "J":
        tur.setheading(0)
        tur.right(90)
        tur.forward(40)
        tur.circle(-20,180)

        tur.circle(-20,-180)
        tur.forward(-40)
        tur.left(90)
        tur.pu()
        tur.forward(10)
        tur.pd()

    elif letter == "K":
        tur.right(90)
        tur.forward(60)
        tur.right(180)
        tur.forward(30)
        tur.right(135)
        tur.forward(45)
        tur.right(180)
        tur.forward(45)
        tur.right(90)
        tur.forward(45)
        tur.setheading(0)



    elif letter == "L":
        tur.pu()
        tur.forward(10)
        tur.pd()
        tur.right(90)
        tur.forward(60)
        tur.left(90)
        tur.forward(30)
        tur.pu()
        tur.forward(10)
        tur.left(90)
        tur.forward(60)
        tur.right(90)
        tur.pd()
        
        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	







window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
turtleLetter("M",tur)
turtleLetter("N",tur)
turtleLetter("O",tur)

turtleLetter("B",tur)
turtleLetter("E",tur)
turtleLetter("H",tur)
turtleLetter("K",tur)
turtleLetter("N",tur)
turtleLetter("Q",tur)
turtleLetter("W",tur)


window.exitonclick()



window.exitonclick()
