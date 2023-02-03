# INSERTION SORT O(n^2)
# O(n) - when the list is already in the correct order

from test import test
from test import check

arr = [2,0,2,1,1,0]

def insertion_sort(arr):
    # for currentIndex in range(1, len(arr)):

    #     i = currentIndex
    #     while i > 0 and arr[i] < arr[i - 1]:
    #         arr[i], arr[i - 1] = arr[i - 1], arr[i]

    #         i -= 1
    for i in range(0, len(arr)):
        key = arr[i] # current value
        j = i - 1 # position to the left

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] 
            j = j - 1
        arr[j + 1] = key

        check(arr)

    print(arr)

print('Numbers test:')
insertion_sort(arr)
print('\n')
insertion_sort(test[0])
