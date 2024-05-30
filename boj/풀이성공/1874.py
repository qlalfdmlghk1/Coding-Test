n = int(input())
numbers = []
stack = []
answer = []
for i in range(n,0,-1) :
    numbers.append(i)

for _ in range(n) :
    k = int(input())
    while numbers and numbers[-1] <= k :
        stack.append(numbers.pop())
        answer.append('+')
    if stack[-1] == k :
        answer.append('-')
        stack.pop()
        continue
    else :
        answer = ["NO"]
        break

for i in answer :
    print(i)