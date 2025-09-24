a = int(input("Give a number: "))
b = int(input("Give another number: "))

try:
    c = a / b
    print('division:', c)
except ZeroDivisionError as e:
    print('exception:', e)
else:
    print('else block executed')
finally:
    print('finally block executed')
