# Program to convert an infix expression to a postfix expression using stacks

def precedence(oper):
    if oper == '+' or oper == '-':
        return 1
    elif oper == '*' or oper == '/':
        return 2
    elif oper == '^':
        return 3
    return 0


oldex = list(input("Enter the infix expression within (): "))
stack = []
newex = []
for i in range(len(oldex)):
    c = oldex[i]
    if c.isalpha():
        newex.append(c)
    if c == '(':
        stack.append(c)
    if c in '+-*/^':
        p = stack.pop()
        if precedence(p) < precedence(c):
            stack.append(p)
            stack.append(c)
        else:
            stack.append(p)
            while precedence(p) >= precedence(c):
                p = stack.pop()
                newex.append(p)
            stack.append(c)
    if c == ')':
        while True:
            p = stack.pop()
            if p != '(':
                newex.append(p)
            else:
                break
print("Postfix expression is: ", *newex, sep='')
