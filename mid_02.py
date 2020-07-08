# 소수 관련 문제는 전형적인 면접용 문제
# 간단하지만 얼마든지 꼬을 수 있고 수학을 얼마나 잘하는지 테스트 가능하기 때문

A = int(input())
bool = ""
for i in range(1, (A + 1) // 2):
    if A % i == 0:
        if i == 1:
            bool = "True"
        else:
            bool = "False"
print(bool)

# 귀류법
# n이 소수가 아니라면, n = a * b (두 개의 정수) 형태로 표현된다.
# a, b 둘 다 root(n)보다 커진다면 a, b 둘 다 root(n) + alpha 형태로 표현되는데,
# 이 때 a, b를 서로 곱할 경우,
# a * b = n + c * d +root(n) * (c + d) 의 형태가 되므로 맨 처음에 n = a * b 이 참이라고 가정한 명제에 모순이 발생한다.

'''
류연수 학우 코드
user_input = int(raw_input())
for i in range(2, int(user_input**0.5)+1):
    if user_input % i == 0:
        print "False"
        break
    else:
        print "True"
'''

'''
강사님 코드
import math

n = int(input())
is_prime = True

if n == 1:
    is_prime = False
else:
    if n % 2 == 0 and n != 2:
        is_prime = False
    else:
        for x in range(3, int(math.sqrt(n)) + 1, 2):
            if n % x == 0:
                is_prime = False
print(is_prime)
'''