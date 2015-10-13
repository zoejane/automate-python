import re
phoneRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume='''
hello 111-222-3333
se 222-333-4444
123-345-5678
'''

mo=phoneRegex.search(resume)
print(mo)
mo=phoneRegex.findall(resume)
print(mo)

phoneRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneRegex.findall(resume)
print(mo)

phoneRegex=re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo=phoneRegex.findall(resume)
print(mo)

digitRegex=re.compile(r'\d')

vowelRegex=re.compile(r'[aeiou]')
mo=vowelRegex.findall('Robocop eats baby food.')
print(mo)
lowercaseRegex=re.compile(r'[a-z]')
mo=lowercaseRegex.findall('Robocop eats baby food.')
print(mo)
