coins, amount = [186,419,83,408], 6249
dp = [10001] * (amount + 1)
dp[0] = 0

for i in range(amount+1) :
    for coin in coins :
        if i + coin <= amount :
            dp[i+coin] = min(dp[i+coin], dp[i]+1)

if dp[amount] == 10001 :
    print(-1)
else :
    print(dp[amount])


