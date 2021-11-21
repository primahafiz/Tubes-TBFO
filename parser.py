import re

terminal=["True", "False", "variable", "class", "is", "return", "None", "continue", "pass", "break", "for", "def", "from", "import", "while", "and", "or", "not", "with", "as", "if", "elif", "else", "range", "print", "open", "in", "raise", "space", "string", "number", "+", "-", "*", "/", "=", "(", ")", ">", "<", "%", ":", "'", '"', ",", "."]

def main_parser(file):
    f=open(file,'r')
    read_file=f.read()
    f.close()
    ops=[r'\+','-',r'\*',r'\\','<','>','=','%',r'\'',r'\"',r'\(',r'\)',':']
    temp=[]
    results=read_file.split("\n")
    lines=[result.split() for result in results]
    # print(lines)
    for op in ops:
        for i in range(len(lines)):
            for line in lines[i]:
                formats=r"("+op+r")"
                split_res=re.split(formats,line)
                for split_string in split_res:
                    if(split_string!=''):
                        temp.append(split_string)
            lines[i]=temp
            temp=[]
    # print(lines)

    variable=r"[a-zA-Z_][a-zA-Z0-9_]*"
    number=r"[0-9]+"

    variable_pattern=re.compile(variable)
    number_pattern=re.compile(number)
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if(variable_pattern.match(lines[i][j]) and (lines[i][j] not in terminal or lines[i][j]=='number')):
                lines[i][j]='variable'
            elif(number_pattern.match(lines[i][j])):
                lines[i][j]='number'
    print(lines)
    return lines

            

file="input.txt"
main_parser(file)
