myCat={'size':'fat',
       'color':'gray',
       'dispositon':'loud'}

print(myCat['size'])
print('My cat has ' + myCat['color']+' fur.')

spam={12345:'Luggage combiation',
      42:'The Answer'}

print(myCat.keys())
print(myCat.values())
print(myCat.items())

print(list(myCat.keys()))
print(list(myCat.values()))
print(list(myCat.items()))

for k in myCat.keys():
    print(k)

for k,v in myCat.items():
    print(k,v)

for i in myCat.items():
    print(i)

print(myCat.get('age',0))
print(myCat.get('color',''))

picnicItems={'apples':5,
             'cups':2}
print('I am bringing '+ str(picnicItems.get('napkins',0)) + ' napkins to the picnic.')

myCat.setdefault('species','cat')
print(myCat)
