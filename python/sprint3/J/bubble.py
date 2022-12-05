from typing import List

def bubble(m: List[int]):
    l = len(m)
    while l > 1:
        previous_m = m.copy()
        for count, value in enumerate(m):
            if count < l - 1:
                next = m[count + 1]
                if value > next:
                    m[count + 1] = value
                    m[count] = next
        if m == previous_m and l < len(m):
            break
        print(*m, sep=" ")
        l -= 1
        previous_m = m.copy()

n = int(input())
massive = list(map(int, input().strip().split()))
bubble(massive)