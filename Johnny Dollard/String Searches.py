name=input("NAME: ")

for letter in name:
    print(letter)

print("\n")

for letter in range(len(name)):
    print(name[letter])
    
print("\n")

letter=0
while letter<len(name):
    print(name[letter])
    letter+=1

print("\n")

letter=len(name)-1
while letter>=0:
    print(name[letter])
    letter-=1

print(name.rfind("c"),name.rfind("m"))
