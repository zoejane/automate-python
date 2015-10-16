import re
namesRegex = re.compile(r'Agent \w+')
mo=namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

mo=namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob.')
print(mo)

namesRegex = re.compile(r'Agent (\w)(\w)\w*')
mo=namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

mo=namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob.')
print(mo)

mo=namesRegex.sub(r'Agent \2****','Agent Alice gave the secret documents to Agent Bob.')
print(mo)
