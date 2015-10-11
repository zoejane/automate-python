##ver1
'''def isPhoneNumber(text):
    if len(text) !=12:
        return False # not phont number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
        if text[3] !='-':
            return False # missing dash
        for i in range(4,7):
            if not text[i].isdecimal():
                return False # no first 3 digits
        if text[7] !='-':
            return False # missing second dash
        for i in range(8,12):
            if not text[i].isdecimal():
                return False # missing last 4 digits
        return True

print(isPhoneNumber('415-555-1234'))

message = 'Call me 415-555-1011 tomorrow,\
or at 415-222-4424.'

foundNumber =False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone nubmers.')'''

##ver2

import re

message = 'Call me 415-555-1011 tomorrow,\
or at 415-222-4424.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(message)
print(mo.group())

mo = phoneNumRegex.findall(message)
print(mo)


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search(message)
print(mo.group(1))
print(mo.group(2))

phoneNumRegex = re.compile(r'\(\d\d\d\)-(\d\d\d-\d\d\d\d)')
message = 'Call me (415)-555-1011 tomorrow,\
or at 415-222-4424.'
mo = phoneNumRegex.search(message)
print(mo.group())



batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel')
print(mo.group())
