#11722 [BOJ] 가장 긴 감소하는 부분 수열 / 실버 2 / 40분

n=int(input())
arr = list(map(int,input().split()))

dp = [1 for _ in range(n)] # 수열의 길이

for i in range(n):
  for j in range(i):
    if arr[j]>arr[i]:
      dp[i]=max(dp[i],dp[j]+1)

print(max(dp))