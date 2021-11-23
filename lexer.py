import re
import sys

terminal=[None, None, "True", "False", "class", "is", "return", "None", "continue", "pass", "break", "for", "def", "from", "import", "while", "and", "or", "not", "with", "as", "if", "elif", "else", "range", "print", "open", "in", "raise", "variable", "comment", "comment", "string", "string", "number", "newline", "+", "-", "*", "/", "=", "(", ")", ">", "<", "%", ":", ",", ".", "[", "]", "&", "|", "^", "~", "!"]

tokenExprs = [
    terminal,
    [
        r'[ \t]+',
        r'#[^\n]*',
        r"\bTrue\b", r"\bFalse\b", 
        r"\bclass\b", r"\bis\b", r"\breturn\b", r"\bNone\b", r"\bcontinue\b", r"\bpass\b", r"\bbreak\b", r"\bfor\b", r"\bdef\b", r"\bfrom\b", r"\bimport\b", r"\bwhile\b", r"\band\b", r"\bor\b", r"\bnot\b", r"\bwith\b", r"\bas\b", r"\bif\b", r"\belif\b", r"\belse\b", r"\brange\b", r"\bprint\b", r"\bopen\b", r"\bin\b", r"\braise\b", 
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
        r"\]",
        r'&',
        r'\|',
        r"\^",
        r"~",
        r'!'
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
