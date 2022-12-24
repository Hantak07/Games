# Character file
import random
from collections import deque
from turtle import *

UP = 90
DOWN = 270

RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.__count = 0
        self.__cords = [(0,0), (-20,0), (-40,0)]
        self.__segments = deque([])
        for i in self.__cords:
            self.element = Turtle(shape="square")
            self.element.penup()
            self.element.color("grey")
            self.element.goto(i[0], i[1])
            self.__segments.append(self.element)
        self.head = self.__segments[0]
        self.__segments[1].color("gainsboro")
        self.head.color("red")

    """Growth function"""
    def extend(self):
        self.__new_segment = Turtle(shape="square")
        if self.__count % 2 == 0:
            self.__new_segment.color("gainsboro")
        else:
            self.__new_segment.color("grey")
        self.__count += 1
        self.__new_segment.penup()
        self.__new_segment_cords = self.__segments[-1].pos()
        self.movebody()
        self.movehead()
        self.__segments.append(self.__new_segment)
        self.__new_segment.goto(self.__new_segment_cords[0], self.__new_segment_cords[1])


    """Movement"""
    def movehead(self):
        self.head.fd(20)

    def movebody(self):
        for i in range(len(self.__segments)-1, 0, -1):
            self.__cords = (self.__segments[i-1].xcor(), self.__segments[i-1].ycor())
            self.__segments[i].goto(self.__cords[0], self.__cords[1])

    """Direction Control"""
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    """Position"""
    def getpos(self):
        return self.head.pos()

    """Collision detection"""
    def detect_collision(self):
        for i in range(1, len(self.__segments) - 1):
            if self.head.distance(self.__segments[i]) < 15:
                return True

    def hide(self):
        for i in self.__segments:
            i.hideturtle()


class RandomDot():
    def __init__(self):
        self.dot = Turtle(shape="circle")
        self.dot.color("green")
        self.dot.penup()
        self.dot.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.dot.speed("fastest")
        self.__pixel = 20

    def gotorandom(self, x, y):
        self.__xcord = random.randrange(-x, x+self.__pixel, self.__pixel)
        self.__ycord = random.randrange(-y, y+self.__pixel, self.__pixel)
        self.dot.goto(self.__xcord, self.__ycord)