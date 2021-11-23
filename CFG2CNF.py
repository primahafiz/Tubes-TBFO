import sys

T = []
V = []
R = [[]]
leftR = []
hash = {}
I = 0

def loadAll(path):
    R = []
    file = open(path).read()
    T = (file.split("Variable:\n")[0].replace("Terminal:\n","").replace("\n","")).split(' ')
    V = (file.split("Rules:\n")[0].split("Variable:\n")[1].replace("Variable:\n","").replace("\n","")).split(' ')
    RArray = (file.split("Rules:\n")[1]).split('\n')
    for i in range(len(RArray)):
        leftRule = RArray[i].split(' -> ')[0]
        rightRule = RArray[i].split(' -> ')[1].split(' | ')
        for j in range(len(rightRule)):
            R.append( (leftRule, rightRule[j].split(' ')) )

    return (T,V,R)

def first(V,R):
    V = ['S0'] + V
    R = [('S0', ['S'])] + R
    return (V,R)

def moreThanTwo(R):
    i = 0
    found = False
    while ((not found) and (i < len(R))):
        if len(R[i][1]) > 2:
            found = True
        else:
            i += 1
    return found

def termVar(V,R):
    i = 0
    found = False
    while ((not found) and (i < len(R))):
        if (len(R[i][1]) == 2):
            if not ((R[i][1][0] in V) and (R[i][1][1] in V)):
                found = True
            else:
                i += 1
        else:
            i += 1
    return found

def unit(V,R):
    i = 0
    found = False
    while ((not found) and (i < len(R))):
        if (len(R[i][1]) == 1):
            if ((R[i][1][0] in V) and not(R[i][1][0] == 'S')):
                found = True
                break
            else:
                i += 1
        else:
            i += 1
    return found


def delRightMoreThanTwo(T,V,R):
    global I
    global hash
    global leftR

    leftR = []
    for rules in R:
        if rules[0] not in leftR:
            leftR.append(rules[0])


    repeat = True
    while repeat:
        if moreThanTwo(R):
            for rules in R:
                if ((rules[1][0] not in T) or (len(rules[1]) > 1)):
                    if (len(rules[1]) > 2):
                        if (len(rules[1]) == 3) and (rules[1][2] in leftR):
                            firstRule = (rules[0], ['V'+ str(I), rules[1][2]])
                            secondRule = ('V'+ str(I), [])
                            three = True
                        else:
                            firstRule = (rules[0], ['V'+ str(I), 'V' + str(I+1)])
                            secondRule = ('V'+ str(I), [])
                            thirdRule = ('V'+ str(I+1), [])
                            three = False
                        for i in range (len(rules[1])):
                            if (i < 2):
                                secondRule[1].append(rules[1][i])
                            elif not three:
                                thirdRule[1].append(rules[1][i])
                        R.remove(rules)
                        if (str(secondRule[1]) in hash):
                            firstRule[1][0] = hash[str(secondRule[1])]
                            firstRule[1][1] = 'V' + str(I)
                            thirdRule = ('V'+ str(I), thirdRule[1])
                            second = False
                        else:
                            if (secondRule[0] not in leftR):
                                hash[str(secondRule[1])] = secondRule[0]
                            second = True
                        if not three:
                            if (str(thirdRule[1]) in hash):
                                firstRule[1][1] = hash[str(thirdRule[1])]
                                third = False
                            else:
                                if (thirdRule[0] not in leftR):
                                    hash[str(thirdRule[1])] = thirdRule[0]
                                third = True
                        R.append(firstRule)
                        if second:
                            R.append(secondRule)
                            V = [secondRule[0]] + V
                            I += 1
                        if not three:
                            if third:
                                R.append(thirdRule)
                                V = [thirdRule[0]] + V
                                I += 1

        else:
            repeat = False
    return (V,R)

def delTermVar(T,V,R):
    global I
    global hash
    global leftR

    repeat = True
    while repeat:
        if termVar(V,R):
            for i in range (len(R)):
                if (len(R[i][1]) == 2):
                    if (R[i][1][0] in T) and (R[i][1][1] in V):
                        if (("['" + str(R[i][1][0]) + "']" in hash)):
                            R[i][1][0] = hash["['" + str(R[i][1][0]) + "']"]
                        else:
                            hash["['" + str(R[i][1][0]) + "']"] = 'V' + str(I)
                            R.append(('V' + str(I), [R[i][1][0]]))
                            R[i][1][0] = 'V' + str(I)
                            V = ['V' + str(I)] + V
                            I += 1
                    elif (R[i][1][1] in T) and (R[i][1][0] in V):
                        if (("['" + str(R[i][1][1]) + "']" in hash)):
                            R[i][1][1] = hash["['" + str(R[i][1][1]) + "']"]
                        else:
                            hash["['" + str(R[i][1][1]) + "']"] = 'V' + str(I)
                            R.append(('V' + str(I), [R[i][1][1]]))
                            R[i][1][1] = 'V' + str(I)
                            V = ['V' + str(I)] + V
                            I += 1
                    elif (R[i][1][1] in T) and (R[i][1][0] in T):
                        if (("['" + str(R[i][1][0]) + "']" in hash)):
                            R[i][1][0] = hash["['" + str(R[i][1][0]) + "']"]
                        else:
                            hash["['" + str(R[i][1][0]) + "']"] = 'V' + str(I)
                            R.append(('V' + str(I), [R[i][1][0]]))
                            R[i][1][0] = 'V' + str(I)
                            V = ['V' + str(I)] + V
                            I += 1
                        if (("['" + str(R[i][1][1]) + "']" in hash)):
                            R[i][1][1] = hash["['" + str(R[i][1][1]) + "']"]
                        else:
                            hash["['" + str(R[i][1][1]) + "']"] = 'V' + str(I)
                            R.append(('V' + str(I), [R[i][1][1]]))
                            R[i][1][1] = 'V' + str(I)
                            V = ['V' + str(I)] + V
                            I += 1
        else:
            repeat = False

    return(V,R)

def delUnit(T,V,R):
    global I
    global hash
    global leftR

    repeat = True
    while repeat:
        if unit(V,R):
            for i in range (len(R)):
                if (len(R[i][1]) == 1) and (R[i][1][0] in V):
                    temp = R[i]
                    R.remove(R[i])
                    for rules in R:
                        if (temp[1][0] == rules[0]):
                            R.append((temp[0], rules[1]))
        else:
            repeat = False
    return (V,R)

def writeRules(R):
    file = open("cnf.txt", 'w')
    dictionary = {}
    result = ""
    for rule in R:
        if rule[0] in dictionary:
            dictionary[rule[0]] += ' | '+' '.join(rule[1])
        else:
            dictionary[rule[0]] = ' '.join(rule[1])
    for key in dictionary:
        result += key + " -> " + dictionary[key]+"\n"
    for i in range (len(result)):
        if i == (len(result) - 1):
            file.write(result[i].rstrip())
        else:
            file.write(result[i])
            
    file.close()

if len(sys.argv) > 1:
    path = str(sys.argv[1])
else:
    path = 'cfg.txt'
        
(T,V,R) = loadAll(path)
(V,R) = first(V,R)
(V,R) = delRightMoreThanTwo(T,V,R)
(V,R) = delTermVar(T,V,R)
(V,R) = delUnit(T,V,R)
writeRules(R)