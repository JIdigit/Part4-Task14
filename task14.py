def d_recursion(n):

    if n < 0:
        print('HIIIIII THERE')
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    if n > 3:
        return d_recursion(n-1) + d_recursion(n-2) + d_recursion(n-3)
    



if __name__ == "__main__":
    s = int(input('How many stairs?\n'))

    for s_itr in range(s):
        n = int(input('How many staricases?\n'))
        res = print(d_recursion(n))

