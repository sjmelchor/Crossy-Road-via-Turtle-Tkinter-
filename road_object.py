from turtle import Turtle


STARTING_POSITIONS = [(-400, -300), (-400, -240), (-400, -140), (-400, -80), (-400, 20), (-400, 80), (-400, 250), (-400, 310)]
roads_list = []

LINE_POSITIONS = [(-410, -270), (-410, -110), (-410, 50), (-410, 280)]
                      
MOVE_DISTANCE = 800

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        
        
        self.speed(0)
        self.draw_road()
        self.draw_lines()
     
        
    def draw_road(self):
        self.color("silver")
        self.pensize(60)
        self.penup()
        self.setheading(0)

        for position in STARTING_POSITIONS:           
            self.goto(position)
            self.pendown()
            self.forward(800)
            self.penup()
            
    def draw_lines(self):
        self.color("yellow")
        self.pensize(10)
        self.penup()
        for position in LINE_POSITIONS:
            self.goto(position)
            for n in range(20):
                self.pendown
                self.forward(20)
                self.penup()
                self.forward(20)
                self.pendown()
                self.forward(20)
                self.penup()


        
##        self.goto(STARTING_POSITIONS[0])
##        self.pendown()
##        self.forward(MOVE_DISTANCE)
##        self.penup()
##        self.goto(STARTING_POSITIONS[1])
##        self.pendown()
##        self.forward(MOVE_DISTANCE)
##        self.penup()
##        self.goto(STARTING_POSITIONS[2])
##        self.pendown()
##        self.forward(MOVE_DISTANCE)



##       
##        
        
        
    





    
