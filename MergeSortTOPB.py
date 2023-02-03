from test import test
from test import check

arr = [2,0,2,1,1,0]

def merge(left, right):
    if not len(left) or not len(right):
        return left or right
  
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break 
  
    return result
  
def mergesort(list):
    if len(list) < 2:
        return list

    
    
  
    middle = len(list)//2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    print(list)
  
    return merge(left, right)
      
print('Numbers test:')
print(mergesort(arr))
print('\n')
print(mergesort(test[0]))
