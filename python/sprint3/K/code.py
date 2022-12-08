def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    n = 0
    for i in range(lf, rg):
        arr[i] = result[n]
        n+=1
        
    return arr


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)

    merge(arr, lf, mid, rg)


func = str(input())
n = int(input())
massive = list(map(int, input().strip().split()))
if func == 'merge':
    massive = merge(massive, 0, n // 2, n)
elif func == 'sort':
    merge_sort(massive, 0, n)
print(*massive, sep=' ')


# def test():
#     a = [1, 4, 9, 2, 10, 11]
#     b = merge(a, 0, 3, 6)
#     expected = [1, 2, 4, 9, 10, 11]
#     assert b == expected
#     c = [17, 7]
#     merge_sort(c, 0 , 2)
#     expected = [7, 17]
#     assert c == expected

# if __name__ == '__main__':
#     test()