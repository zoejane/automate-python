spam =42
cheese = spam
spam=100
print(spam)
print(cheese)


spam=[0,1,2]
cheese=spam
cheese[1]='Hello'
print(cheese)
print(spam)



def eggs(cheese):
    cheese.append('Hello')

spam=[1,2,3]
eggs(spam)

print(spam)



import copy
spam=[0,1,2]
cheese=copy.deepcopy(spam)
cheese[1]='Hello'
print(cheese)
print(spam)

print('a'+
              'b'+
              'c')

print('a'+\
              'b'+\
              'c')
