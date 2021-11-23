import re
import sys

terminal=[None, None, "True", "False", "class", "is", "return", "None", "continue", "pass", "break", "for", "def", "from", "import", "while", "and", "or", "not", "with", "as", "if", "elif", "else", "range", "print", "open", "in", "raise", "variable", "comment", "comment", "string", "string", "number", "newline", "+", "-", "*", "/", "=", "(", ")", ">", "<", "%", ":", ",", ".", "[", "]"]

tokenExprs = [
    terminal,
    [
        r'[ \t]+',
        r'#[^\n]*',
        r"True", r"False", 
        r"class", r"is", r"return", r"None", r"continue", r"pass", r"break", r"for", r"def", r"from", r"import", r"while", r"and", r"or", r"not", r"with", r"as", r"if", r"elif", r"else", r"range", r"print", r"open", r"in", r"raise", 
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',
        r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',
        r'\"[^\"\n]*\"', 
        r'\'[^\'\n]*\'',
        r"[0-9]+",
        r'\n', 
        r'\+', 
        r"\-", 
        r"\*", 
        r"/", 
        r"=", 
        r"\(", 
        r"\)", 
        r">", 
        r"<", 
        r"%", 
        r"\:", 
        r",", 
        r"\.",
        r"\[",
        r"\]"
    ]
]

def conditional_validation(lines):
    conditions=[]
    for content in lines:
        if(content=='if' or content=='elif' or content=='else'):
            conditions.append(content)
    cur_state=0
    for condition in conditions:
        if condition=='if':
            cur_state+=1
        elif condition=='elif' and cur_state>0:
            continue
        elif condition=='else' and cur_state>0:
            cur_state-=1
        else:
            return False
    return True

def main_parser(file):
    f=open(file,'r')
    read_file=f.read()
    f.close()
    # ops=[r'\+','-',r'\*',r'\\','<','>','=','%',r'\(',r'\)',':','\n',r'\.',',',r'\[',r'\]']
    tokens=[]
    pos = 0
    while(pos<len(read_file)):
        match = None
        for i in range(len(tokenExprs[0])):
            pattern = tokenExprs[1][i]
            tag = tokenExprs[0][i]
            regex = re.compile(pattern)
            match = regex.match(read_file, pos)
            if match:
                if tag:
                    tokens.append(tag)
                break
        if not match:
            print(tokens)
            print("Syntax Error")
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

# file="input.txt"
# main_parser(file)
