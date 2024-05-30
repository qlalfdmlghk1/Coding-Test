strn = list(input())
stack=[]
res=''
for s in strn:
    if s.isalpha(): # 알파벳이면 그냥 더한다.
        res += s
    else:
        if s == '(':  # 여는괄호는 무조건 스택에 쌓는다.
            stack.append(s)
        elif s == '*' or s == '/':      # 곱셉 or 나눗셈은 스택이 비어있지 않고, 스택의 마지막이 곱셈이나 나눗셈이라면 결과에 더한다.
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':      # 덧셈 or 뺄셈은 우선순위가 가장 낮으므로 여는 괄호를 만날 때까지 스택에 쌓여있는 연산자 더한다.
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':                  # 닫는 괄호이면, 여는 괄호를 만날 때까지 스택에 쌓여있는 연산자 더한다.
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack :
    res += stack.pop()
print(res)