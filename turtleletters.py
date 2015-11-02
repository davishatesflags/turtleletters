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
        ## comments2
        
        
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
