helloFile = open('hello.txt') # read mode
content=helloFile.read()
helloFile.close()
print(content)

helloFile = open('hello.txt')
print(helloFile.readlines())

# if txt not exit, auto create the file
# write mode:overwrite , start from a blank text
helloFile = open('hello2.txt','w')
helloFile.write('Hello!!!!\n')
helloFile.write('Hello!!!!\n')
helloFile.write('Hello!!!!')
helloFile.close()

import os
print(os.getcwd())

# append mode
helloFile = open('hello3.txt','a')
helloFile.write('Hello')
helloFile.write('Hello!!!!\n')
helloFile.write('Hello!!!!')
helloFile.close()
