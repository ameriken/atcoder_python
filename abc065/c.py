
S = input()
dp = [0] * (len(S) + 1)
dp[0] = 1

words = ["dream", "dreamer", "erase", "eraser"]
done = 'NO'

for i in range(len(S)):
    if dp[i] == 0: continue

    for w in words:
        if S[i:i+len(w)] == w:
            dp[i+len(w)] = 1

    if dp[len(S)] == 1:
        done = 'YES'
        break

print(done)