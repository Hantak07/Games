# Scorboard Module

from turtle import *

class Scorboard():
    def __init__(self):
        self.__board = Turtle()
        self.__board.color("white")
        self.__board.penup()
        self.__score = 0
        self.__board.hideturtle()

    def raisescore(self):
        self.__score += 1

    def setpos(self, x, y):
        self.__board.goto(x, y)

    def write(self):
        self.__board.clear()
        self.__board.write(f"Score : {self.__score}", align="left", font=("Arial", 25, "normal"))

    def gameover(self):
        self.__board.clear()
        self.__board.goto(0,0)
        self.__board.write(f"Gameover\n Score : {self.__score}", align="center", font=("Arial", 25, "normal"))