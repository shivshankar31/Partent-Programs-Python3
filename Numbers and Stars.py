# Numbers and Stars

for row in range(5):
    for col in range(row):
        print(row, end=' ')
    print('* ' * (5-row), end=' ')
    print()
