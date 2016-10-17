'''
Johnny Dollard
Period 4
"If" Lab 2 Discount
'''
def getPrice( ann ):
  if ann>2000:
    ann=ann*0.9
  return ann


print ( getPrice( -11 ) ) 
print ( getPrice( 180 ) )
print ( getPrice( 2170 ) )
print ( getPrice( 3100 ) )
print ( getPrice( 9339 ) )
print ( getPrice( 2001 ) )
