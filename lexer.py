import re

terminal=["True", "False", "variable", "class", "is", "return", "None", "continue", "pass", "break", "for", "def", "from", "import", "while", "and", "or", "not", "with", "as", "if", "elif", "else", "range", "print", "open", "in", "raise", "space", "string", "number", "+", "-", "*", "/", "=", "(", ")", ">", "<", "%", ":", "'", '"', ",", "."]

def main_parser(file):
    f=open(file,'r')
    read_file=f.read()
    f.close()
    ops=[r'\+','-',r'\*',r'\\','<','>','=','%',r'\'',r'\"',r'\(',r'\)',':','\n',r'\.',',',r'\[',r'\]']
    temp=[]
    results=re.split(" +",read_file)
    # print(results)
    lines=results
    for op in ops:
        for content in lines:
            formats=r"("+op+r")"
            split_res=re.split(formats,content)
            for split_string in split_res:
                if(split_string!=''):
                    temp.append(split_string)
        lines=temp
        temp=[]
    # print(lines)
    # print(lines)

    newline='\n'
    variable=r"[a-zA-Z_][a-zA-Z0-9_]*"
    number=r"[0-9]+"

    variable_pattern=re.compile(variable)
    number_pattern=re.compile(number)
    newline_pattern=re.compile(newline)
    
    for i in range(len(lines)):
        if(variable_pattern.match(lines[i]) and (lines[i] not in terminal or lines[i]=='number')):
            lines[i]='variable'
        elif(number_pattern.match(lines[i])):
            lines[i]='number'
        elif(newline_pattern.match(lines[i])):
            lines[i]='newline'
    # print(lines)
    return lines

            

file="input.txt"
main_parser(file)
