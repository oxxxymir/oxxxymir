n = int(input())
flour = 0
space2 = 1
space = ' '
star = '*'
for i in range(1, n + 1):
    flour += 1
    space2 = n - flour
    space = space * space2
    if i == n:
        print(star)
    else:
        print(пробел + star)
    пробел = ' '
    star += '*' * 2