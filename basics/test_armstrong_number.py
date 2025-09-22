number = 154
n = number
r = 0
sum = 0

while n > 0:
    r = n % 10  # r = 3, r = 5, r = 1
    sum = sum + (r * r * r)  # sum = 27, sum = 152, sum = 153
    n = n // 10  # n = 15, n = 1, n = 0

if number == sum:
    print('armstrong number')
else:
    print('not a armstrong number')
