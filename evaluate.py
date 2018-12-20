operate_set = ['+','-','*','/','(',')','#']

def precede(operate_a, operate_b):
    if operate_a == '+' or operate_a == '-':
        if operate_b == '+' or operate_b == '-' or operate_b == ')' or operate_b == "#":
            return '>'
        else:
            return '<'
    elif operate_a == '*' or operate_a == '/':
        if operate_b == '(':
            return '<'
        else:
            return '>'
    elif operate_a == '(':
        if operate_b == ')':
            return '='
        elif operate_b == '#':
            return None
        else:
            return '<'
    elif operate_a == ')':
        if operate_b == '(':
            return None
        else:
            return '>'
    elif operate_a == '#':
        if operate_b == '#':
            return '='
        elif operate_b == ')':
            return None
        else:
            return '<'

def check_is_operate(c):
    if c in operate_set:
        return True
    else:
        return False

def find_operate(expression):
    pos = 1
    for char in expression:
        if check_is_operate(char):
            #print("find operate return pos = " + str(pos))
            return pos
        else:
            pos=pos+1
    #print("find not operate return pos = " + str(pos))
    return pos

def getchar(expression):
    if len(expression) == 0:
        return '#'
    operate_pos = find_operate(expression)
    if operate_pos > 1:
        operate_pos = operate_pos -1
    return_char =  expression[0:operate_pos]
    #print("getchar = " + return_char)
    return return_char

def update(expression):
    if len(expression) == 0:
        return None
    operate_pos = find_operate(expression)
    if operate_pos > 1:
        operate_pos = operate_pos -1
    if operate_pos < len(expression):
        expression = expression[operate_pos:]
        #print("update expression = " + expression)
    else:
        expression = ''
    return expression

def do_operate(a,operate,b):
    result = ''
    if operate == "+":
        result = str(int(a) + int(b))
    elif operate == "-":
        result = str(int(a) - int(b))
    elif operate == '*':
        result = str(int(a)*int(b))
    elif operate == "/":
        result = str(int(a)/int(b))
    print("do_operate: " + a + operate + b + " = " + result)
    return result

#print(check_is_operate(getchar('43+234')))
expression = raw_input("input expression end with # ")
final_expression = expression
optr= []
opnd= []
optr.append('#')
char = getchar(expression)
expression = update(expression)
while char != '#' or optr[-1] != '#':
    if check_is_operate(char) == False:
        #print("opnd.append : " + char)
        opnd.append(char)
        char = getchar(expression)
        expression = update(expression)
    else:
        if precede(optr[-1], char) == '<':
            optr.append(char)
            char = getchar(expression)
            expression = update(expression)
        elif precede(optr[-1], char) == '=':
            optr.pop()
            char = getchar(expression)
            expression = update(expression)
        elif precede(optr[-1], char) == '>':
            operate = optr.pop()
            b = opnd.pop()
            a = opnd.pop()
            opnd.append(do_operate(a,operate,b))

print(final_expression + " = " + opnd[-1])
