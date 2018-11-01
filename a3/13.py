from unicodedata import name
a = {chr(i) for i in range(32, 245) if 'SIGN' in name(chr(i), '')}
print(a)