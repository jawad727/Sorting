# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):

    result = []

    left_pointer = right_pointer = 0

    while left_pointer < len(arrA) and right_pointer < len(arrB):
        if arrA[left_pointer] < arrB[right_pointer]:
            result.append(arrA[left_pointer])
            left_pointer += 1

        else:
            result.append(arrB[right_pointer])
            right_pointer += 1

    result.extend(arrA[left_pointer:])
    result.extend(arrB[right_pointer:])

    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    if len(arr) <= 1:
        return arr
    
    midpoint = int(len(arr) / 2)

    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(left, right)

ary = [5, 3, 4, 1, 2]

# Merge_sort takes in this ary
# It then checks if the length is less than or equal to 1, which it isnt, so we move on
# It then makes a midpoint (index[2])
# everything to the left of the 2nd index (4) gets merge_sorted [5, 3] and so on until there are arrays of single values




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
