A = int(input())
bool = ""
for i in range(1, (A + 1) // 2):
    if A % i == 0:
        if i == 1:
            bool = "True"
        else:
            bool = "False"
print(bool)
