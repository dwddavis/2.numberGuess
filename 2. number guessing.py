
def number_Game():

    from random import randint

    def guess_Number(a, score):
        score = score - 1
        guess = int(input("GUESS A NUMBER (1 to 10)? \n"))


        if guess == a:
            print("you win")
            print("SCORE = ",  score)
            more = input("yes or no?")
            if more == "yes":
                return number_Game()
            else:
                exit()

        else:

            if a - guess < 0:
                print("\n LOWER \n")
            else:
                print("\n HIGHER \n")


            guess_Number(a,score)


    for _ in range(1):
        value = int(randint(1,10))
        guess_Number(value,11)


number_Game()

