# 시간복잡도 n으로 접근
# 합이 최대가 되는 구간 구하기
'''
값                       -3  4   9  -2  -5   8  -3
그 수까지 더했을 때 최대값   -3  4  13  11   6  14  14
그 구간 까지의 최대값       -3  4  13  13  13  14  14
'''

n = int(input())
# 입력 받는 line의 위치 중요
stock_idx = [int(input()) for _ in range(n)]
temp_sum = stock_idx[0]
result = stock_idx[0]
for i in range(1, n):
    temp_sum = max(temp_sum + stock_idx[i], stock_idx[i])
    result = max(temp_sum, result)
#    if result == 0:
#        result = min(stock_idx)
print(result)