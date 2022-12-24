# The Main File
import time

import scoreboard
import character, screen

PIXEL = 20

def main():
    x = 800
    y = 650
    lx = int(x/2 - 2*PIXEL)
    ly = int((y-50)/2 - PIXEL)

    display = screen.Display(height=y, width=x)
    display.setboundary()

    board = scoreboard.Scorboard()
    board.setpos(-lx, int((y-30)/2))
    board.write()

    display.startreading()

    snake = character.Snake()
    food = character.RandomDot()
    food.gotorandom(lx, ly)

    display.readkey(fun=snake.up, key="w")
    display.readkey(fun=snake.down, key="s")
    display.readkey(fun=snake.left, key="a")
    display.readkey(fun=snake.right, key="d")

    display.refresh()
    display.startreading()

    while True:
        cords = snake.getpos()
        if abs(cords[0]) > lx or abs(cords[1]) > ly:
            break
        snake.movebody()
        snake.movehead()
        if snake.detect_collision():
            break
        if snake.head.distance(food.dot) < 15:
            board.raisescore()
            board.write()
            food.gotorandom(lx,ly)
            snake.extend()

        display.refresh()
    snake.hide()
    display.refresh()
    time.sleep(1)
    board.gameover()
    display.refresh()
    display.start()

if __name__ == '__main__':
    main()