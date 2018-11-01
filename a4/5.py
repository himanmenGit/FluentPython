for codec in ['latin_1', 'utf-8', 'utf-16']:
    print(codec, 'E1 Nino'.encode(codec), sep='\t')