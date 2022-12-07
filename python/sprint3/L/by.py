from typing import List

def bike(income: List[int], cost: int, left: int, right: int):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if mid == 0:
        if income[mid] >= cost:
            return 1
        return -1
    if income[mid] >= cost and income[mid - 1] < cost:
        return mid+1
    elif cost <= income[mid]:
        return bike(income, cost, left, mid)
    else:
        return bike(income, cost, mid+1, right)




n = int(input())
income = list(map(int, input().strip().split()))
s = int(input())

print(f'{bike(income, s, 0, n)} {bike(income, 2*s, 0, n)}')