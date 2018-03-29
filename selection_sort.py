#selection sort
#O(n^2)

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = [0]*len(arr)
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr[i] = arr[smallest_index]
        del arr[smallest_index]
    return new_arr
