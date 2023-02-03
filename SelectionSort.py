# SELECTION SORT O(n^2)

from test import test
from test import check

arr = [2,0,2,1,1,0]

def selection_sort(arr):
    currentIndex = 0

    while (currentIndex < len(arr) - 1):
        minimumIndex = currentIndex

        for i in range(currentIndex + 1, len(arr)):
            if (arr[i] < arr[minimumIndex]):
                minimumIndex = i

        arr[currentIndex], arr[minimumIndex] = arr[minimumIndex], arr[currentIndex]     
        currentIndex += 1
        
        check(arr) # CHECK ANSWER

    print(arr)

print('Numbers test:')
selection_sort(arr)
print('\n')
selection_sort(test[0])



