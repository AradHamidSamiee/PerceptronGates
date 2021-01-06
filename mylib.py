import random

def help():
    help_file = open("help.txt")
    for line in help_file:
        print(' ',line,end='')
    print('')

# ----- LINK 1 -----
def test_scan():
    # first link
    # print("  --- SCANNING DATASET INITIATED  ---")
    dataset_file = open("stdo.csv")
    records = 0
    data = dict()
    # generating dictionary keys
    for line in dataset_file:
        for attrib in line.split(','):
            if attrib != '\n' and attrib != line.split(',')[-2]:
                data[attrib] = list()
            elif attrib == line.split(',')[-2]:
                data["desired"] = list()
        break
    temp_keys = list(data.keys())
    for line in dataset_file:
        records += 1
        for t in range(len(temp_keys)):
            # tuple of input and weight
            data[temp_keys[t]].append(((int(line.split(',')[t])),float("{:.1f}".format(random.uniform(0, 1000)/1000))))
            t += 1
    # desired output
    desired = list()
    for smt in data['desired']:
        desired.append(smt[0])
    temp_keys = list(data['desired'])
    del data['desired']
    # print("  --- SCANNING DATASET SUCCESSFUL ---")
    perceptron(data, desired, records)

# ----- PERCEPTRON -----
def perceptron(data, desired, records):
    iepochs = int(input('  How many EPOCHS: '))
    repochs = 0
    LearningRate = float(input('  LearningRate is: '))
    error = 0.0
    result = 0.0
    while repochs != iepochs:
        repochs += 1
        print('\n  -------\n  EPOCH',repochs,'\n ','-------')
        for record in range(records):
            for key in data: # SIGMA X,W
                print('  X:', data[key][record][0], 'W:', data[key][record][1])
                result += data[key][record][0] * data[key][record][1]
            result = sigmoid(result)
            error = desired[record] - result
            print('  result:', result, '| error:', error, '\n  -----')
            if error != 0:
                weight_update(record, data, LearningRate, error)
            result = 0
            error = 0

# ----- UPDATE -----
def weight_update(record, data, LearningRate, error):
    new_weight = 0.0
    for key in data:
        new_weight = float("{:.1f}".format(data[key][record][1] - (LearningRate * error * data[key][record][0])))
        data[key][record] = (data[key][record][0], new_weight)

# ----- SIGMOID -----
def sigmoid(x):
    e = 2.71828
    x = 1 / (1 + e**(-x))
    if x <= 0.5:
        return 0
    else:
        return 1
