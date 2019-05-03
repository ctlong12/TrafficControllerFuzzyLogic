# Intellegent Trafffic Light System
# Math 307 Final Project
# Chandler Long


import sys

waitingTrafficFuzzySet = ['minimal', 'light', 'average', 'heavy', 'standstill']
oncomingTrafficFuzzySet = ['minimal', 'light', 'average', 'heavy', 'excess']

durationFuzzySet = ['short', 'medium', 'long']

fuzzyRules = [[['minimal', 'minimal'], 'short'], [['minimal', 'light'], 'short'], [['minimal', 'average'], 'medium'],
                      [['minimal', 'heavy'], 'long'], [['minimal', 'excess'], 'long'],

                      [['light', 'minimal'], 'short'], [['light', 'light'], 'short'], [['light', 'average'], 'medium'],
                      [['light', 'heavy'], 'medium'], [['light', 'excess'], 'long'],

                      [['average', 'minimal'], 'short'], [['average', 'light'], 'medium'], [['average', 'average'], 'medium'],
                      [['average', 'heavy'], 'long'], [['average', 'excess'], 'long'],

                      [['heavy', 'minimal'], 'medium'], [['heavy', 'light'], 'medium'], [['heavy', 'average'], 'long'],
                      [['heavy', 'heavy'], 'long'], [['heavy', 'excess'], 'long'],
                      
                      [['standstill', 'minimal'], 'medium'], [['standstill', 'light'], 'long'], [['standstill', 'average'], 'long'],
                      [['standstill', 'heavy'], 'long'], [['standstill', 'excess'], 'long']]



def main():
    print('\nStart Program\n')

    carsWaiting = 10
    carsIncoming = 33

    print('Number of cars waiting: ', carsWaiting)
    print('Number of cars incoming: ', carsIncoming)

    #Returns a two dimensional array in the form [['Light', 1.0], ['Average', 0.0]]
    waitingTraffic = carWaitingFunction(carsWaiting)
    incomingTraffic = carIncomingFunction(carsIncoming)


    print('CARS WAITING: ', waitingTraffic, '   CARS INCOMING: ', incomingTraffic)


    possibleWait = infer(waitingTraffic, incomingTraffic, fuzzyRules)

    result = []
    resultMax = {}

    for i in possibleWait:
        print(i[0][0][0][1], i[0][0][0][2], [0][0][1][1], i[0][0][1][2], i[1])
        minimum = min(dt[0][0][0][2], i[0][0][1][2])
        result.append([i[1],minimum])

    for i in resultMax:
        if i[0] in resultMax:
            resultMax[i[0]].add(i[1])
        else:
            resultMax[data[0]] = set([i[1]])

    inference = []
    for key, value in resultMax.items():
        inference.append([key,max(value)])

    print('Deffuzzyfication')
    finalValue = defuzzyfication(inference)

    print('FUZZY SET: ', finalValue)
    
    seconds = secs(finalValue)

    print('Green lights will be activated for ', seconds, ' seconds!')


def secs(values):
    seconds = 0
    
    shortX = 50
    mediumX = 90
    longX = 125

    condition1 = values[0]
    value1 = values[1]
    condition2 = values[2]
    value2 = values[3]

    if condition1 == 'medium' and condition2 == 'short':
        seconds = (value1 * mediumX + value2 * shortX)
    if condition1 == 'medium' and condition2 == 'long':
        seconds = (value1 * mediumX + value2 * longX)
    if condition1 == 'long' and condition2 == 'medium':
        seconds = (value1 * longX + value2 * mediumX)
    if condition1 == 'short' and condition2 == 'medium':
        seconds = (value1 * shortX + value2 * mediumX)
    if condition1 == 'long':
        seconds = 150
    else:
        seconds = 45
    return seconds
    


def defuzzyfication(inputs):
    
    fuzzyValues = []
    
    currentFuzzyLinguistics = 'short'
    currentFuzzyLinguistics2 = 'short'
    currentFuzzyValue = 1.0
    fuzzyDifference = 0

    for i in inputs:
        for j in i:
            if j == 'short':
                if i[1] < currentFuzzyValue:
                    currentFuzzyValue = i[1]
            if j == 'medium':
                if i[1] < currentFuzzyValue:
                    currentFuzzyValue = i[1]
                    currentFuzzyLinguistics = j
            if j == 'long':
                if i[1] < currentFuzzyValue:
                    currentFuzzyValue = i[1]
                    currentFuzzyLinguistics = j
    if currentFuzzyLinguistics == 'medium':
        currentFuzzyLinguistics2 = 'short'
        fuzzyDifference = 1.0 - currentFuzzyValue
    if currentFuzzyLinguistics == 'long':
        currentFuzzyLinguistics2 = 'medium'
        fuzzyDifference = 1.0 - currentFuzzyValue
    else:
        fuzzyDifference = 1.0 - currentFuzzyValue


    fuzzyValues.append(currentFuzzyLinguistics)
    fuzzyValues.append(currentFuzzyValue)
    fuzzyValues.append(currentFuzzyLinguistics2)
    fuzzyValues.append(fuzzyDifference)
    
    return fuzzyValues 


def infer(waiting, oncoming, rules):
    A = []
    P = []

    for i in waiting:
       A.append(i)    
    for i in oncoming:
        A.append(i)
    
    while A:
        x = A.pop(0)    
        for rule in rules: 
            for j, k in enumerate(rule[0]):
                if k == x[0]:
                    rule[0][j] = [True, rule[0][j], x[1]]
            if check(rule[0]):
                result = rule[1]
                P.append(rule)
                A.append(result)
                rule[0] = [rule[0],'processed']

    return P

def check(x):
    for i in x:
        if x[0] != True:
            return False
    return True

def carWaitingFunction(cars):
    linguisticCarsWaiting = []
    
    if cars >= 0 and cars <= 15:
        linguisticCarsWaiting.append(waitingTrafficFuzzySet[0]) # Minimal load of cars waiting
    if cars >= 10 and cars <= 25:
        linguisticCarsWaiting.append(waitingTrafficFuzzySet[1]) # Light load of cars waiting
    if cars >= 20 and cars <= 35:
        linguisticCarsWaiting.append(waitingTrafficFuzzySet[2]) # Average load of cars waiting
    if cars >= 30 and cars <= 45:
        linguisticCarsWaiting.append(waitingTrafficFuzzySet[3]) # Heavy load of cars waiting
    if cars >= 40:
        linguisticCarsWaiting.append(waitingTrafficFuzzySet[4]) # Standstill load of cars waiting




    #Determine the overall wait time     (REVISE)

    valueOfCarsWaiting = []
    
    if len(linguisticCarsWaiting) > 1:
        if linguisticCarsWaiting[0] == waitingTrafficFuzzySet[0] and linguisticCarsWaiting[1] == waitingTrafficFuzzySet[1]:
            #Minimal and Light traffic wating (10 : 15)
            minimal = - (cars - 15) / (15 - 10)
            valueOfCarsWaiting.append([linguisticCarsWaiting[0], minimal])
    
            light = - (cars - 25) / (15 - 10)
            valueOfCarsWaiting.append([linguisticCarsWaiting[1], light])
            
            print('Fuzzy Set Minimal & Light: ', valueOfCarsWaiting)

            return valueOfCarsWaiting
            
        elif linguisticCarsWaiting[0] == waitingTrafficFuzzySet[1] and linguisticCarsWaiting[1] == waitingTrafficFuzzySet[2]:
            #Light and Average traffic waiting
            light = - (cars - 25) / (25 - 20)
            valueOfCarsWaiting.append([linguisticCarsWaiting[0], light])

            average = (cars - 20) / (25 - 20)
            valueOfCarsWaiting.append([linguisticCarsWaiting[1], average])
            
            print('Fuzzy Set Light & Average: ', valueOfCarsWaiting)

            return valueOfCarsWaiting
            
        elif linguisticCarsWaiting[0] == waitingTrafficFuzzySet[2] and linguisticCarsWaiting[1] == waitingTrafficFuzzySet[3]:
            #Average and Heavy traffic waiting
            average = - (cars - 35) / (35 - 30)
            valueOfCarsWaiting.append([linguisticCarsWaiting[0], average])

            heavy = (cars - 30) / (35 - 30)
            valueOfCarsWaiting.append([linguisticCarsWaiting[1], heavy])
            
            print('Fuzzy Set Average & Heavy: ', valueOfCarsWaiting)

            return valueOfCarsWaiting
            
        elif linguisticCarsWaiting[0] == waitingTrafficFuzzySet[3] and linguisticCarsWaiting[1] == waitingTrafficFuzzySet[4]:
            #Average and Heavy traffic waiting
            heavy = - (cars - 45) / (45 - 40)
            valueOfCarsWaiting.append([linguisticCarsWaiting[0], heavy])

            standstill = (cars - 40) / (45 - 40)
            valueOfCarsWaiting.append([linguisticCarsWaiting[1], standstill])
            
            print('Fuzzy Set Heavy & Standstill: ', valueOfCarsWaiting)

            return valueOfCarsWaiting
        else:
            return valueOfCarsWaiting.append([linguisticCarsWaiting[0],1])




def carIncomingFunction(cars):
    linguisticCarsIncoming = []
    
    if cars >= 0 and cars <= 15:
        linguisticCarsIncoming.append(oncomingTrafficFuzzySet[0]) # Minimal load of cars coming into the intersection
    if cars >= 10 and cars <= 25:
        linguisticCarsIncoming.append(oncomingTrafficFuzzySet[1]) # Light load of cars coming into the intersection
    if cars >= 20 and cars <= 35:
        linguisticCarsIncoming.append(oncomingTrafficFuzzySet[2]) # Average load of cars coming into the intersection
    if cars >= 30 and cars <= 45:
        linguisticCarsIncoming.append(oncomingTrafficFuzzySet[3]) # Heavy load of cars coming into the intersection
    if cars >= 40:
        linguisticCarsIncoming.append(oncomingTrafficFuzzySet[4]) # Standstill load of cars coming into the intersection

    print('\nINCOMING CARS FUZZY: ', linguisticCarsIncoming, '\n')

    valueOfCarsIncoming = []
    
    if len(linguisticCarsIncoming) > 1:
        if linguisticCarsIncoming[0] == oncomingTrafficFuzzySet[0] and linguisticCarsIncoming[1] == oncomingTrafficFuzzySet[1]:
            #Minimal and Light traffic wating (10 : 15)
            minimal = - (cars - 15) / (15 - 10)
            valueOfCarsIncoming.append([linguisticCarsIncoming[0], minimal])
    
            light = - (cars - 25) / (15 - 10)
            valueOfCarsIncoming.append([linguisticCarsIncoming[1], light])
            
            print('Fuzzy Set Minimal & Light: ', valueOfCarsIncoming)

            return valueOfCarsIncoming
            
        elif linguisticCarsIncoming[0] == oncomingTrafficFuzzySet[1] and linguisticCarsIncoming[1] == oncomingTrafficFuzzySet[2]:
            #Light and Average traffic waiting
            light = - (cars - 25) / (25 - 20)
            valueOfCarsIncoming.append([linguisticCarsIncoming[0], light])

            average = (cars - 20) / (25 - 20)
            valueOfCarsIncoming.append([linguisticCarsIncoming[1], average])
            
            print('Fuzzy Set Light & Average: ', valueOfCarsIncoming)

            return valueOfCarsIncoming
            
        elif linguisticCarsIncoming[0] == oncomingTrafficFuzzySet[2] and linguisticCarsIncoming[1] == oncomingTrafficFuzzySet[3]:
            #Average and Heavy traffic waiting
            average = - (cars - 35) / (35 - 30)
            valueOfCarsIncoming.append([linguisticCarsIncoming[0], average])

            heavy = (cars - 30) / (35 - 30)
            valueOfCarsIncoming.append([linguisticCarsIncoming[1], heavy])
            
            print('Fuzzy Set Average & Heavy: ', valueOfCarsIncoming)

            return valueOfCarsIncoming
            
        elif linguisticCarsIncoming[0] == oncomingTrafficFuzzySet[3] and linguisticCarsIncoming[1] == oncomingTrafficFuzzySet[4]:
            #Average and Heavy traffic waiting
            heavy = - (cars - 45) / (45 - 40)
            valueOfCarsIncoming.append([linguisticCarsIncoming[0], heavy])

            excess = (cars - 40) / (45 - 40)
            valueOfCarsIncoming.append([linguisticCarsIncoming[1], excess])
            
            print('Fuzzy Set Heavy & Excess: ', valueOfCarsIncoming)

            return valueOfCarsIncoming
            
        else:
            return valueOfCarsIncoming.append([linguisticCarsIncoming[0],1])

            
if __name__ == '__main__':
    main()
