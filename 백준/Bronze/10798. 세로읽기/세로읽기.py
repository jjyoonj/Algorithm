word = [input() for _ in range(5)]

for col in range(15):
    for row in range(5):
        if col < len(word[row]):
            print(word[row][col], end='')