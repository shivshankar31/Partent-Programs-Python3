#Half Inverted Triangle

no = 1
for row in range(5,0,-1):
    for col in range(row):
        print(no, end = ' ')
    print()
    no+=1
