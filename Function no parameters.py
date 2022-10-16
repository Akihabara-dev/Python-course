# English: Functions without parameters
# Spanish: Funciones sin parametros

from random import*

def generateRandom():
    # Return random value Between 1 and 10
    return randint(1,10)

for i in range(0,10):
    # end = " " >>> avoid line break and leave a space between result
    print(generateRandom(), end=" ")