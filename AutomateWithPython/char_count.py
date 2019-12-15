message = 'it was a bright cold day in april, and the clocks were striking thirteen.'
count = {} #'r':12 #pprint,pformat->import pprint

for character in  message.upper():
    count.setdefault(character,0)
    count[character] = count[character]+1

print(count)
