import sys

N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
org = 10
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            res = nums[i]+nums[j]+nums[k]
            if res > M:
                continue
            if M == res:
                print(M)
                sys.exit()
            if abs(M-res) < abs(M-org):
                org = res
print(org)