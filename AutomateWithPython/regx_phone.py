import re

message = 'Call me 415-555-1546 tomorrow and office number is 415-555-5443'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)#phoneNumRegex.findall(message)
print(mo.group())

