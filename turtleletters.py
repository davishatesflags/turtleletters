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

        
	## Zach
	
	## Noah
	
	## Joe
	
	## Desmond
	
	## Addison
    	

        ## Brian


        ## Ryan
	
	## Hunter
  
        
        
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
