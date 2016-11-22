import time
import sys

def guessCheck(guess, number):
    if guess>number:
        print("Too Big!")
    if guess<number:
        print("Too Small!")

def roundSummary(guesses, limit, rounds, totalGuesses, score):
    print("Guesses:",guesses,"\n+",limit*10-guesses,"Points")
    if limit!=rounds:
        print("\nTotal guesses so far:",totalGuesses,"\nScore so far:",score)
    time.sleep(1)

def gameSummary(AILevel, totalGuesses, score, totalGuesses2, score2, totalCompGuesses, compScore):
    #Game Summary
    if AILevel==0:
        print ("\n\nTotal Guesses:",totalGuesses,"\nScore:",score)
        sys.exit()
    
    elif AILevel==6:
        print ("\n\nPLAYER 1:\nTotal Guesses:",totalGuesses,"\nScore:",score,"\n\nPLAYER 2:\nTotal Guesses:",totalGuesses2,"\nScore:",score2)
        if score>score2:
            print("\n\nPLAYER 1 WINS!")
        if score<score2:
            print("\n\nPLAYER 2 WINS!")
        if score==score2:
            print("\n\nTIE!")
        
    else:
        print ("\n\nYOU:\nTotal Guesses:",totalGuesses,"\nScore:",score,"\n\nCOMPUTER:\nTotal Guesses:",totalCompGuesses,"\nScore:",compScore)
        if score>compScore:
            print("\n\nYOU WIN!")
        if score<compScore:
            print("\n\nYOU LOSE!")
        if score==compScore:
            print("\n\nTIE!")
