import math
def stdDev(arr):
    num =  len(arr)
    mean = sum(arr) / num
    deviations = [(val - mean) ** 2 for val in arr]
    variance = sum(deviations)/ num
    stdDeviation = math.sqrt(variance)
    print(round(stdDeviation, 1))

if __name__ == '__main__':
    n = int(input().strip())
    values = list(map(int, input().rstrip().split()))
    stdDev(values)