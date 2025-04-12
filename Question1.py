# strings = [
#     "abc123",
#     "hello456world",
#     "789",
#     "test"
# ]

# digits = [char for s in strings for char in s if char.isdigit()]
# print(digits)


strings = [
"abc123",
"hello456world",
"789",
"test"
]

ans=[char for row in strings for char in row ]

digits = []
for string in strings:
    for char in string:
        if char.isdigit():
            digits.append(int(char))
print(digits)
print(ans)