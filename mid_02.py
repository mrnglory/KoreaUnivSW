# 소수 관련 문제는 전형적인 면접용 문제
# 간단하지만 얼마든지 꼬을 수 있고 수학을 얼마나 잘하는지 테스트 가능

A = int(input())
bool = ""
for i in range(1, (A + 1) // 2):
    if A % i == 0:
        if i == 1:
            bool = "True"
        else:
            bool = "False"
print(bool)

'''
user_input = int(raw_input())
for i in range(2, int(user_input**0.5)+1):
    if user_input % i == 0:
        print "False"
        break
    else:
        print "True"
'''