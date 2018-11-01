metro_data = [
    ('Tokyo', 'JP', 36, (35.2, 139.6)),
    ('Delhi NCR', 'IN', 21, (28.6, 77.2)),
    ('Mexico City', 'MX', 20, (19.4, -99.1)),
    ('New York-Newark', 'US', 20, (40.8, -74.0)),
    ('Sao Paulo', 'BR', 19, (-23.5, -46.6))
]

from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))
