#gets a dictionary of unique values and their counts
def freq(input, skip, startat):
    binDict = {}
    f = open(input, 'rb')
    for x in range(startat):
        f.read(1)
    while True:
        chunk = f.read(1)
        if not chunk:
            break
        for i in range(skip - 1):
            f.read(1)
        else:
            if chunk in binDict.keys():
                binDict[chunk] += 1
            else:
                binDict[chunk] = 1
    f.close()
    return binDict

#returns a dictionary with coincidences for each character.
# as the Counts of displacement between characters
def coinc(uniqueChars, input):
    coinciDict = {}
    distance = 0
    for i in uniqueChars:
        freqByte = i
        f=open(input, 'rb')
        firstFind = False
        while True:
            chunk = f.read(1)
            if not chunk:
                break
            if chunk == freqByte:
                firstFind = True
                if distance in coinciDict.keys():
                    coinciDict[distance] +=1
                elif distance > 0:
                    coinciDict[distance] = 1
                distance = 1
            elif firstFind == True:
                distance +=1
    f.close()
    return coinciDict

def lengthGuess(inputDict):
    guessDict = {}
    for x in inputDict:
        count = 0
        multiples = 0
        for i in inputDict:
            if i % x == 0:
                multiples += 1
                count += inputDict[i]
        guessDict[x] = (float(count)/float(multiples))
    return guessDict

#Prints out a dictionary to CSV for frequency analysis
def writeDictCSV(dict, fileOutName):
    fo = open(fileOutName + '.csv', 'w')
    fo.write('Distance' + ','+'Count' + '\n')
    for i in dict:
        fo.write(str(i) + "," + str(dict[i]) + "\n")
    fo.close()

inputfile = 'out.txt'
binDictOut = freq(inputfile, 0, 0)
coinciDict = coinc(binDictOut, inputfile)
prob = lengthGuess(coinciDict)
keylength = max(prob, key=prob.get)
password = ""
for i in range(keylength):
    binDictOut = freq(inputfile, keylength, i)
    password += max(binDictOut, key=binDictOut.get)
print "-------XOR Cracker Results-------"
print "The key length is probably: " + str(keylength)
print "The password might be: " + password
