n = int(input())
nums = list(map(int, input().split()))
nums.sort()
sum = 0
median = 0

#Calculating Mean
for i in range(n):
    sum += nums[i]
mean = sum / n

#Calculating Median
mid = n//2
if n % 2 == 0:
    median = (nums[mid] + nums[mid - 1]) / 2
else:
    median = nums[mid]

#Calculating Mode
dict = {}
for i in nums:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
max_val = max(dict.values())
mode_list = [key for key, val in dict.items() if val == max_val]
mode = min(mode_list)

print(round(mean, 1), round(median, 1), mode, sep = '\n')
