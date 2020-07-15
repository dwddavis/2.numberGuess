import random

def doorGame():
    top = random.randint(0,1)
    right = random.randint(0,1)
    left = random.randint(0,1)

    print(" __", top, "__\n", left, "   ", right,"\n")

    if top == 1 and right == 1 and left == 1:
        move = input("left, top, right?")
        return doorGame()

    elif top == 0 and right == 0 and left == 0:
        print("Sorry It's a Dead end")
        return exit()

    elif top == 0 and right == 1 and left == 1:
        move = input("right, left?")
        return doorGame()

    elif top == 0 and right == 0 and left == 1:
        move = input("left?")
        return doorGame()

    elif top == 0 and right == 1 and left == 0:
        move = input("right?")
        return doorGame()

    elif top == 1 and right == 0 and left == 1:
        move = input("top, left?")
        return doorGame()

    elif top == 1 and right == 0 and left == 0:
        move = input("top?")
        return doorGame()



doorGame()