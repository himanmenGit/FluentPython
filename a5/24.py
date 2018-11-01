from collections import namedtuple

metro_data = [
    ('Tokyo', 'JP', 36, (35.2, 139.6)),
    ('Delhi NCR', 'IN', 21, (28.6, 77.2)),
    ('Mexico City', 'MX', 20, (19.4, -99.1)),
    ('New York-Newark', 'US', 20, (40.8, -74.0)),
    ('Sao Paulo', 'BR', 19, (-23.5, -46.6))
]

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]

print(metro_areas)

print(metro_areas[0].coord.lat)
from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))