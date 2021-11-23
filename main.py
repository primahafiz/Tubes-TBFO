import lexer
import cyk

# Load Chomsky Normal Form
chomskyDict = cyk.LoadCNF("cnf.txt")

print(chomskyDict)
print(len(chomskyDict))

# Tokenize
tokens = lexer.main_parser("inputAcc.txt")

print(tokens)
print(len(tokens))
print("abis tokenized")

# Validasi if elif else
isConditionValid=lexer.conditional_validation(tokens)

# CYK
cykTable = cyk.cyk(tokens, chomskyDict)

for row in cykTable:
    print(row)

if(cyk.verdict(cykTable) and isConditionValid):
    print("Accepted")
else:
    print("Syntax Error")