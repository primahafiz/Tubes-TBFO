import re

terminal=["True", "False", "variable", "class", "is", "return", "None", "continue", "pass", "break", "for", "def", "from", "import", "while", "and", "or", "not", "with", "as", "if", "elif", "else", "range", "print", "open", "in", "raise", "space", "string", "number", "+", "-", "*", "/", "=", "(", ")", ">", "<", "%", ":", "'", '"', ",", ".", "[", "]", "&", "|", "^", "~", "!"]
lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','2','3','4','5','6','7','8','9','0']

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

def is_variable(arr,startpos,endpos):
    if arr[startpos] in terminal:
        return False
    else:
        if(arr[startpos][0] in lowercase or arr[startpos][0] in uppercase or arr[startpos][0] == '_'):
            for i in range(1,len(arr[startpos])):
                if arr[startpos][i] in lowercase or arr[startpos][i] in uppercase or arr[startpos][i] == '_' or arr[startpos][i] in number:
                    continue
                else:
                    return False
            return True
        else:
            return False

def is_number(arr,startpos,endpos):
    for i in range(len(arr[startpos][0])):
        if arr[startpos][i] in number:
            continue
        else:
            return False
    return True

def is_string(arr,startpos,endpos):
    if arr[startpos] == "'":
        pos=0
        for i in range(startpos+1,endpos):
            if arr[i] == "'":
                pos=i
                return pos
    if arr[startpos] == '"':
        pos=0
        for i in range(startpos+1,endpos):
            if arr[i] == '"':
                pos=i
                return pos
        return pos
    else:
        return 0

def is_comment(arr,startpos,endpos):
    if arr[startpos] == '#':
        pos=endpos-1
        for i in range(startpos+1,endpos):
            if(arr[i]=='\n'):
                pos=i-1
                return pos
        return pos
    else:
        return 0

def is_multilinecomment(arr,startpos,endpos):
    if endpos-startpos > 2:
        if(arr[startpos]=='"' and arr[startpos+1]=='"' and arr[startpos+2]=='"'):
            state=0
            for i in range(startpos+3,endpos):
                if arr[i] == '"':
                    state+=1
                else:
                    state=0
                if(state==3):
                    return i
    if endpos-startpos > 2:
        if(arr[startpos]=="'" and arr[startpos+1]=="'" and arr[startpos+2]=="'"):
            state=0
            for i in range(startpos+3,endpos):
                if arr[i] == "'":
                    state+=1
                else:
                    state=0
                if(state==3):
                    return i
        return 0
    else:
        return 0
    
def is_newline(arr,startpos,endpos):
    return arr[startpos]=='\n'

def main_parser(file):
    f=open(file,'r')
    read_file=f.read()
    f.close()
    ops=[r'\+','-',r'\*',r'\\','<','>','=','%',r'\'',r'\"',r'\(',r'\)',':','\n',r'\.',',',r'\[',r'\]',r"\'\'\'",r'\"\"\"', r"\[", r"\]", r"\&", "\|", "\^", "~", "\!"]
    temp=[]
    results=re.split(" +",read_file)
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
    print(lines)
    pos=0
    while(pos<len(lines)):
        loc_comment=is_comment(lines,pos,len(lines))
        loc_string=is_string(lines,pos,len(lines))
        loc_multilinecomment=is_multilinecomment(lines,pos,len(lines))
        if (loc_multilinecomment):
            lines[pos:loc_multilinecomment+1]=['multilinecomment']*1
        elif (loc_string):
            lines[pos:loc_string+1]=['string']*1
        elif (loc_comment):
            lines[pos:loc_comment+1]=['comment']*1
        elif (is_variable(lines,pos,len(lines))):
            lines[pos]='variable'
        elif (is_number(lines,pos,len(lines))):
            lines[pos]='number'
        elif is_newline(lines,pos,len(lines)):
            lines[pos]='newline'
        pos+=1
    print(lines)
    return lines