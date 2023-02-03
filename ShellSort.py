# SHELL SORT
# WORST O(n^2)
# BEST O(n*log n) When the array is already sorted, the total number of 
# comparisons for each interval (or increment) is equal to the size of the array.


from test import test
from test import check

arr = [2,0,2,1,1,0]

def shell_sort(arr):
    n = len(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
            print(arr)
            check(arr)
            
        interval //= 2
        

    
        

                   

    print(arr)

print('Numbers test:')
shell_sort(arr)
print('\n')
shell_sort(test[0])