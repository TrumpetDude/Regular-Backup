'''
Johnny Dollard
Period 4
List Lab 3
'''
def find_smallest( ann, val ):
  cnt = 0
  for item in ann:
    if item==val:
      cnt+=1
  return cnt


bob = [3,5,6,33,111,7,7,15,-5,9,1,6,6,7,8,9,5,6,6,6,7,2,7,99,11,8]
print ( find_smallest( bob, 6 ) )
print ( find_smallest( bob, 7 ) )
print ( find_smallest( bob, 5 ) )
