def degerate_valid_combination(n):
    #Base:The base case of our problem is n=0 which return an empty list []
    #parameter n = int
    #Worse case : retutn dp[n]-list of valid combination of the problem
    if n == 0:
        return []
    dp = [ [] for _ in range(n+1)]
    dp [0]= [""]
    #Traverse through the element
    for i in range(1,n+1):
        for j in range(i):
            for x in dp[j]:
                for y in dp[i-j-1]:
                    dp[i].append('(' + x + ')' + y)
    return dp[n]
n = 4
result = degerate_valid_combination(n)
print(result)                