#crossy road main
from turtle import Turtle, Screen
from road_object import Road

#STARTING_POSITIONS = [(-400, -200), (-400, -100), (-400, 200), (-400, 250)]
roads_list = []

#make objects from our classes
turtle = Turtle()
screen = Screen()
road = Road()


#set up the screen with the grass in the background
screen.setup (width = 800, height=800)
screen.bgcolor("sea green")

screen.exitonclick()
