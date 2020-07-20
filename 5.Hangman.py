import random

wordBank = ["messy room", "sleepy baby", "sandwich meat", "pepperoni pizza", "junk food", "scary clowns",
            "pesto and pasta", "sweet and sour cause", "cream cheese bagel", "double cheeseburger", "candied apples",
            "italian sausage", "baby shark song"]

def gamePlay():
    gameWord = random.randint(0, len(wordBank)-1)
    counter = -1
    roundWord = (wordBank[int(gameWord)])
    print(roundWord)
    blankWord = []

    for i in roundWord:
        if ord(i) > 96:
            blankWord.append(ord(i))
        else:
            blankWord.append("_")

    print(blankWord)
    print(len(blankWord))
    print(len(roundWord))

    def oneRound():

        letterUsed = []
        print("\n\nLetters Used", letterUsed)
        print("---|---")

        #print(counter)
        userGuess = input("Guess a Letter \n")
        letterUsed.append(userGuess)

        print(letterUsed)

    oneRound()
gamePlay()