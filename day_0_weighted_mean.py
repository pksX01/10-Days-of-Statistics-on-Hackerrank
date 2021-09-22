def weightedMean(X, W):
    #1st method
    #product = [X[i] * W[i] for i in range(n)]
    
    #2nd method
    product = [x * w for x, w in zip(X, W)]
    print(round(sum(product) / sum(W), 1))

if __name__ == '__main__':
    n = int(input().strip())
    values = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    weightedMean(values, weights)