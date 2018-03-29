#worst case: O(log n)
# O(n):linear time
# O(log n): logarithmic time
# O(n!): factorial time
# O(log n) < O(n) < O(n * log n) < O(n^2) < O(n!)

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
