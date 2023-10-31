def BinarySearch(target, iterable):
    start =0
    end = len(iterable)-1
    while end >= start:
        mid = start + (end - start)//2
        if iterable[mid] == target:
            return mid
        elif iterable[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return -1