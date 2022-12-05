n = int(input())
massive = list(map(str, input().strip().split()))

def is_first_number_bigger(str1: str, str2: str):
    a = int(str1 + str2)
    b = int(str2 + str1)
    return a > b
        

def insertion_sort_by_comparator(array, bigger):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and bigger(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    return print(*array, sep='')


insertion_sort_by_comparator(massive, is_first_number_bigger) 