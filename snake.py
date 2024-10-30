from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.parts=[]
        self.create_snake()
        self.head=self.parts[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)



    def add_part(self,position):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.parts.append(part)

    def extend(self):
        #add new part to the snake
        self.add_part(self.parts[-1].position())


    def move(self):


        for pnum in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[pnum - 1].xcor()
            new_y = self.parts[pnum - 1].ycor()
            self.parts[pnum].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)




