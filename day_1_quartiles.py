def calculate_median(data):
    num = len(data)
    if num % 2 == 0:
        return (data[num//2 - 1] + data[num//2]) // 2
    return data[num//2]

def quartiles(arr):
    arr.sort()
    if n % 2 == 0:
        firstHalfData = arr[ : n//2]
        secondHalfData =  arr[n//2 : ]
          
    else:
        firstHalfData = arr[ : n//2]
        secondHalfData = arr[n//2 + 1 : ]
    
    quartile1 = calculate_median(firstHalfData)
    quartile2 = calculate_median(arr)
    quartile3 = calculate_median(secondHalfData)

    return [quartile1, quartile2, quartile3]

if __name__ == '__main__':
    n =  int(input().strip())
    data = list(map(int, input().rstrip().split()))
    print(quartiles(data))