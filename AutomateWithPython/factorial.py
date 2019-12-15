import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)


def factorial(n):
    logging.debug('Start of factorial({})' .format(n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is {} ,total is {}' .format(i, total))

    logging.debug('Return value is {}' .format(total))
    return total

print(factorial(5))


logging.debug('End of program')
