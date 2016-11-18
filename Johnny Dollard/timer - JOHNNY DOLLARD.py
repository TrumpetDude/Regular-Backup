'''
Johnny Dollard
Period 4
Assignment: Loops Lab 3
'''
import pygame

# Ask user for number of seconds
seconds=int(input("How many seconds? "))


# Loop while seconds are greater than 0
# This makes sure that there is not a delay when "0 seconds" are left
while seconds>0:

    # Part 1 - Print the time left as seconds
    print(seconds)
    # Part 2 - Print the time left as minutes and seconds
    print(seconds//60,":",seconds%60)

    # Wait and change seconds
    pygame.time.wait(1000)
    seconds-=1

print(seconds)
print(seconds//60,":",seconds%60)
