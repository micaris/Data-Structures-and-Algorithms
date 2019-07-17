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

X = "AGGTAB"
Y = "GXTXAYB"
#print(len(S), len(T))
#

n = 3
m = 3 
arr =[ [ 0 for i in range(m)] for i in range(n)]
print(lcs(X, Y))
