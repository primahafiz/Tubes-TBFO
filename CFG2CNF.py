import sys

K = []
V = []
R = [[]]

def loadAll(path):
    R = []
    file = open(path).read()
    K = (file.split("Variable:\n")[0].replace("Terminal:\n","").replace("\n","")).split(' ')
    V = (file.split("Rules:\n")[0].split("Variable:\n")[1].replace("Variable:\n","").replace("\n","")).split(' ')
    RArray = (file.split("Rules:\n")[1]).split('\n')
    for i in range(len(RArray)):
        leftRule = RArray[i].split(' -> ')[0]
        rightRule = RArray[i].split(' -> ')[1].split(' | ').replace(" ","")
        for j in range(len(rightRule)):
            R.append( (leftRule, rightRule[j].split(' ')) )

    return (K,V,R)

def first(V,R):
    V = ['S0'] + V
    R = [('S0', ['S'])] + R
    return (V,R)





if len(sys.argv) > 1:
    path = str(sys.argv[1])
else:
    path = 'cfg.txt'
        
(K,V,R) = loadAll(path)
(V,R) = first(V,R)