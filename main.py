import lexer
import cyk
import sys

if len(sys.argv) > 1:
    path = str(sys.argv[1])

    # Load Chomsky Normal Form
    chomskyDict = cyk.LoadCNF("cnf.txt")

    # print(chomskyDict)
    # print(len(chomskyDict))

    # Tokenize
    tokens = lexer.main_parser(path)

    # Validasi if elif else
    isConditionValid=lexer.conditional_validation(tokens)

    # CYK
    cykTable = cyk.cyk(tokens, chomskyDict)

    if(cyk.verdict(cykTable) and isConditionValid):
        print("Accepted")
    else:
        print("Syntax Error")
else:
    print("Error, please input file name")
