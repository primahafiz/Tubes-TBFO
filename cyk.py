import re

def LoadCNF(cnfPath): # mengembalikan dictionary {Body : [head1, head2, ..]}
    chomskyDict = {}
    f = open(cnfPath,'r')
    f_contents = f.readline()
    while(len(f_contents)>0):
        f_contents = f_contents.strip()
        head, bodies = f_contents.split(' -> ')
        bodies = bodies.split(' | ')
        # bodies = bodies.replace(' ', '') # yang ruas kanannya 2 varaibel bkl jd VAR1VAR2, kalo ga ambigu gpp
        for body in bodies:
            if(chomskyDict.get(body)==None):
                chomskyDict.update({body: [head]})
            else:
                chomskyDict[body].append(head)
        f_contents = f.readline()
    f.close()

    return chomskyDict

def cyk(tokens, chomskyDict):
    n = len(tokens)
    print(n)
    cykTable = [[set() for j in range(n-i)] for i in range(n)]

    #inisialisasi cykTable[0] berisi variable dengan ruas kanan rule terminal i
    for i in range(n):
        if(chomskyDict.get(tokens[i])!=None):
            cykTable[0][i] = set(chomskyDict[tokens[i]])
    
    for i in range(1,n): # tinggi i+1
        for j in range(n-i):
            for k in range(i): # tinggi nya k+1 dan i-k
                # string[j..j+i], dibentuk dari string[j..j+k] dan string[j+k+1..j+i]
                for var1 in cykTable[k][j]:
                    for var2 in cykTable[i-k-1][j+k+1]:
                        if(chomskyDict.get(var1+' '+var2)!=None):
                            cykTable[i][j].update(chomskyDict[var1+' '+var2])
    
    for i in range(n):
        for j in range(n-i):
            if(len(cykTable[i][j])==0):
                cykTable[i][j] = list()

    return cykTable

def verdict(cykTable):
    try:
        return ('S' in cykTable[-1][0])
    except IndexError:
        return False