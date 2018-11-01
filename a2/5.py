symbols = '!@#@!#'
tu = tuple(ord(symbol) for symbol in symbols)
print(tu)

import array
tu = array.array('I', (ord(symbol) for symbol in symbols))
print(tu)