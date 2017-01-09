lowerlimit=int(input("Lower Limit: "))
upperlimit=int(input("Upper Limit: "))
import random
import time
number=random.randint(lowerlimit,upperlimit)
guess=.1
while guess!=number:
    guess=int(input("Guess: "))
    if guess>number:
        print("Too Big!")
    if guess<number:
        print("Too Small!")
print("Correct!")
time.sleep(1)
