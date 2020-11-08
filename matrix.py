# Calculate the sums of even and odd elemens of matrix

from random import randint as rndnt

width = 2
height = 2
Sum_even = 0
Sum_odd = 0
for x in range(0, height, 1):
    Row = []
    for y in range(0, width, 1):
        N = rndnt(0, 100)
        Row.append(N)
        if N % 2 == 0:
            Sum_even += N
        else:
            Sum_odd += N
    for char in Row:
        print(str(char) + " | ", end='')
    print("\n")
print("This is the result of odd elements : %d" % Sum_odd)
print("This is the result of even elements : %d" % Sum_even)
