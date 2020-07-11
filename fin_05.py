'''
(note)
X.X...X.X 의 결과값이 3인 이유: 그냥 9개의 펜스를 통째로 갈아치우는 것,
즉 sqrt(9) == 3 이 제일 가성비 좋기 때문에 굳이 따로 수리할 필요가 없었음

ff[i] = i번째 fibonacci 수
d[i] = 0번째 펜스부터 i번째 펜스까지 고려했을 때의 최소 비용
0번째부터 counting 하므로 n개의 펜스라면 n - 1 번째 까지 고려하면 됨

(example)
[X..X..X...X]...X 라는 데이터가 있다고 하자.
d[6] (혹은 d[9]) + sqrt(1)
d[5] + sqrt(5)
d[3] + sqrt(8)
sqrt(11) ==> d[10]
-> d[0]만 제대로 구하면 그 후의 값들을 제대로 구할 수 있다.
    -> X면 d[0] = 1, .이면 d[0] = 0

즉 fibonacci와 같은 맥락이다.

'''
from math import sqrt
from math import floor

t = int(input())
fence = [str(input()) for _ in range(t)]
price = [0] * t
cnt = [0] * t
for i in range(t):
    for j in range(len(fence[i])):
        if fence[i][j:j+3] == 'X.X':
            cnt[i] += 1
            if cnt[i] % 2 == 0:
                price[i] = round(sqrt(3), 3) * cnt[i]
            else:
                price[i] = round(sqrt(3), 3) + 1
print('\n'.join(map(str, price)))