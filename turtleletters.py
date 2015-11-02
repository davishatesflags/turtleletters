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

	## Matt 

        
	## Zach
	
	## Noah
	
	## Joe
	
	## Desmond
	
	## Addison
    	

        ## Brian


        ## Ryan
	
	## Hunter
    elif letter == "Jx":
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

    elif letter == "Kx":
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



    elif letter == "Lx":
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
	tur.pd
        
        
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
