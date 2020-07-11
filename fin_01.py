n = int(input())
nums = list(map(int, input().split()))
a, b = map(int, input().split())
print(sum(nums[a - 1:b]))