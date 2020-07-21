import random

wordBank = ["messy room", "sleepy baby", "sandwich meat", "pepperoni pizza", "junk food", "scary clowns",
            "pesto and pasta", "sweet and sour cause", "cream cheese bagel", "double cheeseburger", "candied apples",
            "italian sausage", "baby shark song"]

def gamePlay():
    gameWord = random.randint(0, len(wordBank)-1)
    roundWord = (wordBank[int(gameWord)])
    print(roundWord)
    blankWord = []

    for i in roundWord:
        if ord(i) > 96:
            blankWord.append("_")
        else:
            blankWord.append(" ")

    letterUsed=[]
    cleanWord = ""
    

    def oneRound():
        
        tick = -1
        count = -1
        print("\n\n\n", cleanWord.join(blankWord))
        print("Tries Left", tries)
        print("\n\nLetters Used", letterUsed)

        userGuess = input("Guess a Letter \n")
        letterUsed.append(userGuess)

        for j in roundWord:
            tick = tick + 1

            if userGuess == j:
                blankWord[tick] = userGuess
            else:
                count = count + 1

        if count == tick:
            

        oneRound()

    oneRound()
gamePlay()
