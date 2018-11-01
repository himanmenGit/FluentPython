metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.848484, 139.128931)),
    ('Deku BCR', 'IN', 21.935, (28.13555, 77.553535)),
    ('Mexico', 'MX', 20.142, (19.43333, -99.13333)),
    ('New York', 'US', 20.104, (40.488448, -74.020384)),
    ('Sao pult', 'BR', 19.695, (-23.123049, -46.149879)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))