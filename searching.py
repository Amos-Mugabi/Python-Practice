

x = [1,4,6,8,12,15]

def binary_search(a, target, start, stop):
    min = start
    max = stop - 1

    while min <= max:
        mid = (min + max) // 2
        if a[mid] < target:
            min = mid + 1
        elif a[mid] > target:
            max = mid - 1
        else:
             return mid     #target found
    return - (min + 1) #target not found
print(binary_search(x, 12, 0, len(x)))
