def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        
        mid = (high + low) // 2
        print('State: {low} | {high} | {mid}'.format(low=low, high=high, mid=mid))
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
        
    return -1


somel = [1, 2, 3, 4, 5, 6, 7, 8, 20, 44]

value = binary_search(somel, 44)

print(sum([1, 2, 3, 4, 5]))