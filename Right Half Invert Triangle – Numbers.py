# Right Half Invert Triangle – Numbers

for row in range(6):
    for col in range(row):
        print(' ', end=' ')
    for i in range(5-row):
        print(i+1, end=' ')
    print()
