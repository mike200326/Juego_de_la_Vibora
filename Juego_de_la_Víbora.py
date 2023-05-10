from turtle import *
from random import randrange
from freegames import square, vector
from random import choice


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Creemos una lista de colores para que la víbora cambie de color
colors = ['black', 'blue', 'brown', 'cyan', 'gray']
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

# generamos una función para que la comida se mueva aleatoriamente
    dx = randrange(-1, 2)
    dy = randrange(-1, 2)
    food_move = vector(dx, dy)
    food_new = food + food_move

    # revisamos que la comida no se salga de los límites
    if inside(food_new, 10):
        food = food_new

    update()
    ontimer(move, 100)
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