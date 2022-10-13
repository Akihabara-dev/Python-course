# English: 
# 1. The str() function returns representations of the values ​​that are quite human readable
# 2. I While repr() generates representations that can be given to it by the interpreter.

# Spanish: 
# 1. La función str() devuelve representaciones de los valores que son bastante legible por humanos
# 2. Mientras que repr() genera representaciones que le pueden ser dadas por el interprete.

import datetime

today = datetime.datetime.now()

print (str(today))
print (repr(today))
