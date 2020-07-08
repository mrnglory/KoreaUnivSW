'''brackets = list(str(input()))
bool = False
count1 = 0
count2 = 0
count3 = 0
if len(brackets) % 2 == 0:
    for i in range(len(brackets)):
        if brackets[i] == "(":
            count1 += 1
        elif brackets[i] == ")":
            count1 -= 1
        if brackets[i] == "{":
            count2 += 1
        elif brackets[i] == "}":
            count2 -= 1
        if brackets[i] == "[":
            count3 += 1
        elif brackets[i] == "]":
            count3 -= 1
    if count1 == 0 and count2 == 0 and count3 == 0:
        bool = True
else:
    bool = False
print(bool)
'''