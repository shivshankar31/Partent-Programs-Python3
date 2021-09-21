# Left Half Invert Triangle

for row in range(5):
    for col in range(row):
        print(' ', end=' ')
    print('* ' * (5 - row), end=' ')
    print()
