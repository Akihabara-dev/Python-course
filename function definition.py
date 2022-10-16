# English: Function definition
# Example >>> def nameFunction(arguments):
#                ...
#                body function
#                ...
#                return type variable

# Spanish: Definición de funciones

from math import*

def logarithm(x, y):
    logBase = log10(y)
    result = log10(x)/logBase
    return result

print (logarithm(4,2))