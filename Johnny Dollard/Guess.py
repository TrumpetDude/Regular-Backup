lowerlimit=int(input("Lower Limit: "))
upperlimit=int(input("Upper Limit: "))
import random
number=random.randint(lowerlimit,upperlimit)
guess=0
while guess!=number:
    guess=int(input("Guess: "))
    if guess>number:
        print("Too Big!")
    if guess<number:
        print("Too Small!")
print("Correct!")
import time
time.sleep(1)
