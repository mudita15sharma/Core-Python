number = 153
n = number
r = 0
sum = 0

while n > 0:
    r = n % 10  # r = 1, r = 2, r = 1
    sum = (sum * 10) + r  # sum = 1, sum = 12, sum = 121
    n = n // 10  # n = 12, n = 1, n = 0

if number == sum:
    print('Palindrome')
else:
    print('not a Palindrome', sum)
