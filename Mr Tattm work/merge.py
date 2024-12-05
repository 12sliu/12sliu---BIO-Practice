def merge(arr1, arr2):
    newarr = []
    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) == 0:
            return newarr + arr2
        elif len(arr2) == 0:
            return newarr + arr1
        newarr.append(arr2.pop(0) if arr1[0] > arr2[0] else arr1.pop(0))

print(merge([2, 3, 4, 5, 6, 9, 11, 14], [1, 4, 56]))
