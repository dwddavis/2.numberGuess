import random

wordBank = ["messy", "room", "sleepy", "baby", "sandwich", "meat", "pepperoni", "pizza", "junk", "food", "scary",
            "clowns", "pesto", "pasta", "sweet", "sour", "cream", "cheese", "bagel", "double", "cheeseburger",
            "candy", "apples", "italian", "sausage", "shark", "song"]
gamenumber = []


def gamePlay():
    gameWord = random.randint(0, len(wordBank)-1)
    roundWord = (wordBank[int(gameWord)])
    blankWord = []
    letterUsed = []
    cleanWord = ""
    counter = []


    for i in roundWord:
        if ord(i) > 96:
            blankWord.append("_")
        else:
            blankWord.append(" ")




    def oneRound():

        if roundWord == cleanWord.join(blankWord):
            print("\n\n\n\n\nCONGRATZ YOU WIN!!\n\n")
            again = input("\n\n\nPLAY AGAIN (Y or N)?\n\n\n\n")
            if again == "Y" or again == "y":
                gamenumber.append("a")
                gamePlay()
            else:
                return print("bye bye champ")
            return

        elif len(counter) == 6:
            print("\n\n\n\n\n\nSORRY YOU LOSE!!\n\n")
            again = input("\n\n\nPLAY AGAIN (Y or N)?\n\n\n\n")
            if again == "Y" or again == "y":
                gamenumber.append("a")
                gamePlay()
            else:
                return print("bye bye loser")
            return

        yup = 0
        tick = -1
        print("\n\nGame #", len(gamenumber)+1)
        print("\n\n\n", cleanWord.join(blankWord), "                Turns Left", 6-len(counter))
        print("\nUsed", letterUsed)



        userGuess = input("\n\n\n\nGuess a Letter    ")
        letterUsed.append(userGuess)

        for j in roundWord:
            tick = tick + 1

            if userGuess == j:
                yup = yup + tick
                blankWord[tick] = userGuess

        if yup == 0:
            counter.append("a")

        oneRound()






    oneRound()
gamePlay()