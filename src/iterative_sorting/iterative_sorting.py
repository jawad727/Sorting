# TO-DO: Complete the selection_sort() function below 
ary = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arry = [7, 3, 0, 6, 9, 2, 4, 8, 5, 1]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        
        
    return arr



   


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

    



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    print(arr)