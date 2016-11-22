'''
Current Problems:
AI Guesses should be put in methods
Incomplete sections:
AI Levels 2 and 4
2=Random but wont guess a number twice
4=Always guesses right in middle of max/mid range
'''
#Import methods
from Guessv3Methods import *

#Clear Screen
for clear in range (30):
    print("\n")
#Import necessary libraries and set variables
from random import randint
from time import sleep
import sys
totalGuesses=0
score=0
rounds=int(input("Rounds to Play: "))
AILevel=int(input("\n0=Single Player\n1=Monkey On Keyboard\n2=Not Entirely Stupid\n3=Basic AI\n4=Efficient AI\n5=Cheater\n6=Two Players\nAI Level: "))
userNum=0
compGuess=0
totalCompGuesses=0
compScore=0
totalGuesses2=0
score2=0

#MAIN GAME LOOP
#Increases range of guesses until correct # of rounds has been played.
for limit in range(1,rounds+1):
    print("\nRound",limit)
    if limit==rounds:
        print("Last Round!")

    #You Guess Computer's Number
    if AILevel==6:
        print("PLAYER 1")
    print("Guess The Number from 1 to",limit*10)
    number=randint(1,limit*10)
    guess=0
    
    guesses=0
    while guess!=number and guesses<limit*10:
        guess=int(input("\nGuess: "))
        guessCheck(guess, number)
        guesses=guesses+1

    #Increase score and total guesses        
    totalGuesses=totalGuesses+guesses
    score=score+limit*10-guesses
    if guess==number:
        print("Correct!")
    
    #Adds bonus points for first try
    if guesses==1:
        print("First Try! +",limit*10,"Points!")
        score=score+limit*10

    roundSummary(guesses, limit, rounds, totalGuesses, score)
    
    #Computer Guesses Your Number
    
    #Inputting your number
    if AILevel!=0 and AILevel!=6:
        userNum=int(input("\nNumber for computer to guess: "))
        if userNum>limit*10 or userNum<1:
            print("CHEATER!!!!!\nGAME OVER!!!!\nYOU LOSE!!!!!")
            sys.exit()
            
    #Methods need to be defined in a separate program

    if AILevel==1:
        currentCompGuess=0
        compGuesses=0
        while userNum!=currentCompGuess and compGuesses<limit*10:
            sleep(1)
            currentCompGuess=randint(1,limit*10)
            print("\nComputer's Guess:",currentCompGuess)
            if currentCompGuess>userNum:
                print("Too Big!")
            if currentCompGuess<userNum:
                print("Too Small!")
            compGuesses=compGuesses+1
        totalCompGuesses=totalCompGuesses+compGuesses
        compScore=compScore+limit*10-compGuesses
        if currentCompGuess==userNum:
            print("Correct!")
        if compGuesses==1:
            print("First Try!\n+",limit*10,"Points!")
            compScore=compScore+limit*10
        print("Guesses:",compGuesses,"\n+",limit*10-compGuesses,"Points")
        if limit!=rounds:
            print("Total computer guesses so far:",totalCompGuesses,"\nComputer's score so far:",compScore)
        sleep(1)
        
    if AILevel==2:
        pass
    
    
    if AILevel==3:
        currentCompGuess=0
        compGuesses=0
        maxCompGuess=limit*10
        minCompGuess=1
        while userNum!=currentCompGuess and compGuesses<limit*10:
            sleep(1)
            if minCompGuess==maxCompGuess:
                if minCompGuess==1:
                    maxCompGuess=2
                if maxCompGuess==limit*10:
                    minCompGuess=limit*10-1
            currentCompGuess=randint(minCompGuess,maxCompGuess)
            print("\nComputer's Guess:",currentCompGuess)
            if currentCompGuess>userNum:
                print("Too Big!")
                maxCompGuess=currentCompGuess-1
            if currentCompGuess<userNum:
                print("Too Small!")
                minCompGuess=currentCompGuess+1
            compGuesses=compGuesses+1
        totalCompGuesses=totalCompGuesses+compGuesses
        compScore=compScore+limit*10-compGuesses
        if currentCompGuess==userNum:
            print("Correct!")
        if compGuesses==1:
            print("First Try!\n+",limit*10,"Points!")
            compScore=compScore+limit*10
        print("Guesses:",compGuesses,"\n+",limit*10-compGuesses,"Points")
        if limit!=rounds:
            print("Total computer guesses so far:",totalCompGuesses,"\nComputer's score so far:",compScore)
        sleep(1)
        
    if AILevel==4:
        pass
    
    if AILevel==5:
        totalCompGuesses=totalCompGuesses+1
        compScore=compScore+limit*10-1
        print("\nComputer's Guess:",userNum,"\nCorrect!\nFirst Try!\n+",limit*10,"Points!")
        compScore=compScore+limit*10
        print("Guesses:",1,"\n+",limit*10-1,"Points")
        if limit!=rounds:
            print("Total computer guesses so far:",totalCompGuesses,"\nComputer's score so far:",compScore)
        sleep(1)

    if AILevel==6:
        print("\nPLAYER 2\nGuess The Number from 1 to",limit*10)
        number2=randint(1,limit*10)
        guess2=0
        
        guesses2=0
        while guess2!=number2 and guesses2<limit*10:
            guess2=int(input("\nGuess: "))
            guessCheck(guess2, number2)
            guesses2=guesses2+1

        
        #Increase score and total guesses        
        totalGuesses2=totalGuesses2+guesses2
        score2=score2+limit*10-guesses2
        if guess2==number2:
            print("Correct!")
        
        #Adds bonus points for first try
        if guesses2==1:
            print("First Try! +",limit*10,"Points!")
            score2=score2+limit*10

        roundSummary(guesses2, limit, rounds, totalGuesses2, score2)
    
    
gameSummary(AILevel, totalGuesses, score, totalGuesses2, score2, totalCompGuesses, compScore)
