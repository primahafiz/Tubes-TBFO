import sys

T = []
V = []
R = [[]]
I = 0

def loadAll(path):
    R = []
    file = open(path).read()
    K = (file.split("Variable:\n")[0].replace("Terminal:\n","").replace("\n","")).split(' ')
    V = (file.split("Rules:\n")[0].split("Variable:\n")[1].replace("Variable:\n","").replace("\n","")).split(' ')
    RArray = (file.split("Rules:\n")[1]).split('\n')
    for i in range(len(RArray)):
        leftRule = RArray[i].split(' -> ')[0]
        rightRule = RArray[i].split(' -> ')[1].split(' | ')
        for j in range(len(rightRule)):
            R.append( (leftRule, rightRule[j].split(' ')) )

    return (K,V,R)

def first(V,R):
    V = ['S0'] + V
    R = [('S0', ['S'])] + R
    return (V,R)

def moreThanTwo(R):
    ii = 0
    found = False
    while ((not found) and (ii < len(R))):
        if len(R[ii][1]) > 2:
            found = True
        else:
            ii += 1
    return found

def delRightMoreThanTwo(T,V,R):
    global I

    hash = {}
    for i in range(len(R)):
        if (len(R[i][1]) == 1) and (R[i][1] in T):
            hash[str(R[i][1])] = R[i][0]

    two = True
    while two:
        if moreThanTwo(R):
            for rules in R:
                if ((rules[1][0] not in T) or (len(rules[1]) > 1)):
                    if (len(rules[1]) > 2):
                        firstRule = (rules[0], ['V'+ str(I), 'V' + str(I+1)])
                        secondRule = ('V'+ str(I), [])
                        thirdRule = ('V'+ str(I+1), [])
                        for i in range (len(rules[1])):
                            if (i < 2):
                                secondRule[1].append(rules[1][i])
                            else:
                                thirdRule[1].append(rules[1][i])
                        R.remove(rules)
                        if (str(secondRule[1]) in hash):
                            firstRule[1][1] = hash[str(secondRule[1])]
                            thirdRule = ('V'+ str(I), thirdRule[1])
                            second = False
                        else:
                            if (len(secondRule[1]) == 1) and (secondRule[1][0] in T):
                                hash[str(secondRule[1])] = secondRule[0]
                            second = True
                        if (str(thirdRule[1]) in hash):
                            firstRule[1][1] = hash[str(thirdRule[1])]
                            third = False
                        else:
                            if (len(thirdRule[1]) == 1) and (thirdRule[1][0] in T):
                                hash[str(thirdRule[1])] = thirdRule[0]
                            third = True
                        R.append(firstRule)
                        if second:
                            R.append(secondRule)
                            V = [secondRule[0]] + V
                            I += 1
                        if third:
                            R.append(thirdRule)
                            V = [thirdRule[0]] + V
                            I += 1

        else:
            two = False
    return (V,R)



if len(sys.argv) > 1:
    path = str(sys.argv[1])
else:
    path = 'cfg.txt'
        
(T,V,R) = loadAll(path)
(V,R) = first(V,R)
(V,R) = delRightMoreThanTwo(T,V,R)
for rules in R:
    print(rules)