'''
Johnny Dollard
Period 4
"If" - LEAP YEAR LAB
'''
while ( True ):
    # Get the numerator
    year = int(input("Enter a year :: "))


    # check to see if it is a leap year
    # a leap year is divisible by 4 and / or 400
    if year%4==0 or year%400==0:
    
    
    
        # print leap year if it is a leap year
        print(year,"is a leap year.")
    
    
        # print not a leap year if it is NOT a leap year
    else:
        print(year,"is NOT a leap year.")
