'''
Johnny Dollard
Period 4
Assignment Lab 2 on loops
'''
while ( True ):
    # enter a number
    num = int(input("Enter a number :: "))

    numSum = 0
    cnt=0
    
    while num!=0:
        #sum digit
        numSum+=num%10
        #chop off right most digit
        num=int(num/10)
        #Add to count
        cnt+=1
    print(numSum/cnt)
