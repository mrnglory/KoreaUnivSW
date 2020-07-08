string = list(input())
stack = []
for i in range(len(string)-1, -1, -1):
    stack.append(string[i])
print("".join(map(str, stack)))