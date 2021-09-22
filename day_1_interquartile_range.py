def calculate_median(data):
    num = len(data)
    if num % 2 == 0:
        return (data[num//2 - 1] + data[num//2]) / 2
    return data[num//2]

def quartiles(arr):
    arr.sort()
    num = len(arr)
    if num % 2 == 0:
        firstHalfData = arr[ : num//2]
        secondHalfData =  arr[num//2 : ]
          
    else:
        firstHalfData = arr[ : num//2]
        secondHalfData = arr[num//2 + 1 : ]
    
    quartile1 = calculate_median(firstHalfData)
    quartile3 = calculate_median(secondHalfData)

    return quartile1, quartile3

def interQuartile(values, freqs):
    data = []
    for i in range(n):
        data += [values[i]] * freqs[i]
    
    q1, q3 = quartiles(data)
    print(round(float(q3 - q1), 1))

if __name__ == '__main__':
    n =  int(input().strip())
    values = list(map(int, input().rstrip().split()))
    freqs = list(map(int, input().rstrip().split()))
    interQuartile(values, freqs)