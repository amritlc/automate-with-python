'''

*************
*           *
*           *
*           *
*************

'''

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string of lenght 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" cant be less then 2.')
    
    print(symbol*width)

    for i in range(height-2):
        print(symbol+(' ' *(width - 2)) + symbol)

    print(symbol * width)

boxPrint('*',15,5)

boxPrint('+',5,15)



