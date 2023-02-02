from test import test
import numpy as np

arr = [2,0,2,1,1,0]

def insertion_sort(arr):
    for currentIndex in range(1, len(arr)):

        i = currentIndex
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

            i -= 1

    
        
        ### CHECK ##############################
        a1 = np.array(test[0])
        for index, array in enumerate(test):
           
            if np.array_equal(a1, array):
                match index:
                    case 1:
                        print('ANSWER IS - ** B **')
                    case 2:
                        print('ANSWER IS - ** C **')
                    case 3:
                        print('ANSWER IS - ** D **')
                    case 4:
                        print('ANSWER IS - ** E **')
                    case 5:
                        print('ANSWER IS - ** F **')
                    case 6:
                        print('ANSWER IS - ** G **')
                    case 7:
                        print('ANSWER IS - ** H **')
                    case 8:
                        print('ANSWER IS - ** I **')
                    case 9:
                        print('SORTING COMPLETED SUCCESSFULLY!\n')
        #######################################
                   

    print(arr)

print('Numbers test:')
insertion_sort(arr)
print('\n')
insertion_sort(test[0])
