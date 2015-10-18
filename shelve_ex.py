import shelve
# list,dictionary,etc..

shelfFile =shelve.open('mydata')
shelfFile['cats']=['Pooka','Simon','Cleo']
shelfFile.close()

shelfFile =shelve.open('mydata')
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
