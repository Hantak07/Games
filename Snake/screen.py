# Display Module

import time
from turtle import *

class Display():
    def __init__(self, height, width):
        self.__pixel = 20
        self.__height = height
        self.__width = width
        self.__lx = int(width/2) - self.__pixel
        self.__ly = int(height/2) - self.__pixel
        self.__screen = Screen()
        self.__screen.setup(height=self.__height, width=self.__width)
        self.__screen.bgcolor("black")
        self.__screen.tracer(0)

    def setboundary(self):
        for i in range(-self.__ly, self.__ly+self.__pixel, self.__pixel):
            self.__brick1 = Turtle(shape="square")
            self.__brick2 = Turtle(shape="square")
            self.__brick1.color("white")
            self.__brick2.color("white")
            self.__brick1.shapesize(stretch_len=0.3)
            self.__brick2.shapesize(stretch_len=0.3)
            self.__brick2
            self.__brick1.penup()
            self.__brick2.penup()
            self.__brick1.goto(-self.__lx, i)
            self.__brick2.goto(self.__lx, i)

        for i in range(-self.__lx, self.__lx+self.__pixel, self.__pixel):
            self.__brick1 = Turtle(shape="square")
            self.__brick2 = Turtle(shape="square")
            self.__brick1.color("white")
            self.__brick2.color("white")
            self.__brick1.shapesize(stretch_wid=0.3, stretch_len=1)
            self.__brick2.shapesize(stretch_wid=0.3, stretch_len=1)
            self.__brick1.setheading(0)
            self.__brick2.setheading(0)
            self.__brick1.penup()
            self.__brick2.penup()
            self.__brick1.goto(i, -self.__ly)
            self.__brick2.goto(i, self.__ly)

    def refresh(self):
        time.sleep(0.1)
        self.__screen.update()

    def startreading(self):
        self.__screen.listen()

    def clear(self):
        self.__screen.reset()

    def readkey(self, fun, key):
        self.__screen.onkeypress(fun=fun, key=key)

    def start(self):
        self.__screen.exitonclick()
