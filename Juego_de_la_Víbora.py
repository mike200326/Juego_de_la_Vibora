from turtle import *
from random import randrange
from freegames import square, vector
from random import choice

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Creemos una lista de colores para que la víbora cambie de color
colors = ['black', 'blue', 'yellow', 'cyan', 'gray']
# Elegimos un color aleatorio de la lista
random_color = choice(colors)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, random_color)

    square(food.x, food.y, 9, random_color)
    update()
    ontimer(move, 100)
    ontimer(move_food, 500)  
    # tiempo de espera para que la comida se mueva

def move_food():
    # Movimiento de la comida de forma aleatoria
    steps = [-10, 10]
    food_move = vector(choice(steps), choice(steps))
    food.move(food_move)

    if not inside(food):
        food.x = food.x - food_move.x
        food.y = food.y - food_move.y

    update()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()