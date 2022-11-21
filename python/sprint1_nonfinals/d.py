from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    length = len(temperatures)
    randomness = 0
    if length == 1:
        return 1
    if temperatures[0] > temperatures[1]:
        randomness += 1
    if temperatures[length - 1] > temperatures[length -2]:
        randomness += 1
    for i in range(1, length-1):
        a = temperatures[i]
        if (a > temperatures[i + 1]
            and a > temperatures[i - 1]):
            randomness += 1
    return randomness

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
