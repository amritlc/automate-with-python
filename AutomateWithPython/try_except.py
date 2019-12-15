'''
def div(divideby):
    try:
        
        return 42/divideby
    except: #ZeroDivisionError:
        print('You try to divide by zero.')

print(div(2))
print(div(12))
print(div(0))
print(div(1))
'''

print('How many cats do you have ')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is alot of cats')
    else:
        print('That  is not many cats. ')
except:
    print('You must enter numeric values')
