#Import necessary libraries and set variables
from random import randint
from time import sleep
totalGuesses=0
score=0
rounds=int(input("Rounds to Play: "))

#Increases range of guesses until correct # of rounds has been played
for limit in range(1,rounds+1):
    print("\nRound",limit)
    
    if limit==rounds:
        print("Last Round!")
    print("Guess The Number from 1 to",limit*10)
    number=randint(1,limit*10)
    guess=0

    guesses=1
    while guess!=number:
        guess=int(input("\nGuess: "))
        if guess>number:
            print("Too Big!")
            guesses=guesses+1
        if guess<number:
            print("Too Small!")
            guesses=guesses+1

    #Increase score and total guesses        
    totalGuesses=totalGuesses+guesses
    score=score+limit*10-guesses
    print("\nCorrect!")
    
    #Adds bonus points for first try
    if guesses==1:
        print("First Try! +",limit*10,"Points!")
        score=score+limit*10

    #Round summary
    print("Guesses:",guesses,"\n+",limit*10-guesses,"Points")

    #This prevents repeating info of the last round in the game summary
    if limit!=rounds:
        print("Total guesses so far:",totalGuesses,"\nScore so far:",score)
    sleep(1)
#Game Summary   
print ("\n\nYou Win! \nTotal Guesses:",totalGuesses,"\nScore:",score)
