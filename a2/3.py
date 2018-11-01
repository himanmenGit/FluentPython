symbols = '(&@*$!'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 39]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 39, map(ord, symbols)))
print(beyond_ascii)
