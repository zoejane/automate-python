message = 'It was a bright cold day in April.'
count={} # 'r':12 times

for character in message.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1
print(count)


import pprint

pprint.pprint(count)

text=pprint.pformat(count)
print(text)
