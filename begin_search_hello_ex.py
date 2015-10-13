import re
beginsWithHelloRegex=re.compile(r'^Hello')
mo=beginsWithHelloRegex.search('Hello there!')
print(mo)
mo=beginsWithHelloRegex.search('He said "Hello there!"')
print(mo)

endsWithWorldRegex=re.compile(r'there$')
mo=endsWithWorldRegex.search('He said Hello there')
print(mo)

allDigitsRegex=re.compile(r'^\d+$')
mo=allDigitsRegex.search('2333333')
print(mo)

atRegex=re.compile(r'.at')
mo=atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

atRegex=re.compile(r'.{1,2}at')
mo=atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
mo=nameRegex.findall('First Name: Zoe Last Name: Jane')
print(mo)

serve='<To serve humans> for dinner.>'

nongreedy=re.compile(r'<(.*?)>')
mo=nongreedy.findall(serve)
print(mo)

greedy=re.compile(r'<(.*)>')
mo=greedy.findall(serve)
print(mo)
