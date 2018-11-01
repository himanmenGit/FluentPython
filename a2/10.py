from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.69994, 139.69554))
print(tokyo)

print(tokyo.population)
print(tokyo.coordinates)

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.12394, 77.220383))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)

