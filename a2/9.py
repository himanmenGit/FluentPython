from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.69994, 139.69554))
print(tokyo)

print(tokyo.population)
print(tokyo.coordinates)