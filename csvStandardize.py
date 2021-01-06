input_file = input('> bad csv file: ')
with open(input_file, 'r') as istr:
    with open('stdo.csv', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + ','
            print(line, file=ostr)
