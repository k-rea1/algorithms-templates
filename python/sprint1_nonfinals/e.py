def get_longest_word(line: str) -> str:
    longest = max(line.split(), key=len)
    return longest

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
