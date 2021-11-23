import lexer
import cyk

# Load Chomsky Normal Form
chomskyDict = cyk.LoadCNF("cnf.txt")

print(chomskyDict)
print(len(chomskyDict))

# Tokenize
tokens = lexer.main_parser("input3.txt")

print(tokens)
print(len(tokens))
print("abis tokenized")

# CYK
cykTable = cyk.cyk(tokens, chomskyDict)

for row in cykTable:
    print(row)

if(cyk.verdict(cykTable)):
    print("Accepted")
else:
    print("Syntax Error")
    



