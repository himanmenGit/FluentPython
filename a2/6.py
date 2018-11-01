colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('{!s} {!s}'.format(c, s) for c in colors for s in sizes):
    print(tshirt)