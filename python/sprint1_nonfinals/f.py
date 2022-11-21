def is_palindrome(line: str) -> bool:
    letter_line = []
    for char in line:
        if char.isalpha():
            letter_line.append(char.lower())
    letter_line_normal = letter_line.copy()
    letter_line.reverse()
    return letter_line_normal == letter_line

print(is_palindrome(input().strip()))
