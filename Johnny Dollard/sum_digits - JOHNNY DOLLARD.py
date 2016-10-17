'''
Johnny Dollard
Periood 4
Assignment: Lab 1 on loops
'''
while ( True ):
    # enter a number
    num = int(input("Enter a number :: "))

    numSum = 0
    
    while num!=0:
        #sum digit
        numSum+=num%10
        #chop off right most digit
        num=int(num/10)
    print(numSum)
