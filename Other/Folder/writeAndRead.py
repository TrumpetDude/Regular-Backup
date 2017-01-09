import os
#Import the library for finding directories (folders)
#and paths (locations of files)

os.chdir(os.path.dirname(os.path.realpath(__file__)))
'''
os.path.realpath - get the path of the current file (__file__ or 'nameOfFile.py'.
*Can be used on anything (doesn't have to be current file ('name.extention')
os.path.dirname - extract the directory from the path of the current file
(get the path of the foler it's in)
os.chdir - change the current working directory (where files are written, etc. cwd for short.)
'''

print('Current Working Directory:\t'+os.getcwd())
#Show that the cwd has changed

textFile = open('newFile.txt','w')
#create a new plain text file (or overwrite a prevoius one of the same name) called newFile
#and set it to a variable (textFile) that can be modified in write mode ('w')

textFile.write('\nWriting to\nText File')
#Put the string into the text file
#Be careful about putting quotes into your text file. It won't read them later on unless thay are escaped with a backslash

textFile.close()
#Close the text file

textFile = open('newFile.txt','r')
#re-open the file in read mode ('r')

print(textFile.read())
#print the entire contents of the file

textFile.close()
#close the text file

newProgram = open('newProgram.py','w')
#Same as before, except this is a python script instead of a text file

newProgram.write('print("\\nThis is in a brand new python script!")')
'''
Put code into the new script.
Notice the double quotes vs single quotes. When using a different type,
you don't have to escape using a backslash.
However, I did have to escape the backslash that I used
to pass \n (new line) to the new program with a second backslash.
'''

newProgram.close()
#close the new program

import newProgram
#run the new program
#This will create a __pycache__ folder just like importing methods does

'''
The output should look like this:

Current Working Directory:	/Users/Johnny/Desktop/Python/Other/Folder

Writing to
Text File

This is in a brand new python script!
'''
#The first line will change
#The next two were read from newFile.txt
#The last bit was what the new program did!

'''
Other info:

-There is also an append mode ('a') that you can use to add text to an existing file
rather than replacing the contents

-Using the readlines() methos rather than just read() will return a list of strings
(each index is a line from the file)
'''
