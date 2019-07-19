def LCS(S, n, T, m, arr):
    if (n < 0 or m < 0):
        return 0
    
    if( S[n] == T[m]):
        arr[m][n] = 1 + LCS(S, n-1, T, m-1, arr)
    else:
        result = max(LCS(S, n-1, T, m, arr), LCS(S, n, T, m-1, arr))
        arr[m][n] = result
        print(arr)
    return result

def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
  
    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1): 
        for j in range(n+1): 
            if (i == 0 or j == 0) : 
                L[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L
#end of function lcs 

# X = "AGGTAB"
# Y = "GXTXAYB"
# #print(len(S), len(T))
# #

# n = 3
# m = 3 
# arr =[ [ 0 for i in range(m)] for i in range(n)]
# print(lcs(X, Y))

#****************************KNAPSACK PROBLEM****************#

items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )

def totalvalue(comb):
    totwt = totalval = 0
    for item, wt, val in comb:
        totwt += wt 
        totalval += val 
    return (totalval, -totwt) if totwt <= 400 else(0, 0)



def knapsack01_dp(items, limit):

    table = [[0 for w in range(limit + 1)] for j in range(len(items)+ 1)]

    for j in range(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in range(1, limit + 1):
            if wt > w:
                table[j][w] = table[j -1][w]
            else:
                table[j][w] = max(table[j-1][w], table[j-1][w-wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt

    return result

