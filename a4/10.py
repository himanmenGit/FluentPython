fp = open('cafe.txt', 'w', encoding='utf=8')
print(fp)

print(fp.write('café'))

fp.close()

import os
print(os.stat('cafe.txt').st_size)

fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)

print(fp2.read())

fp3 = open('cafe.txt', encoding='utf-8')
print(fp3)

print(fp3.read())

fp4 = open('cafe.txt', 'rb')
print(fp4)

print(fp4.read())