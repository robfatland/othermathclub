def add_them_up(n, a):
    if a == n:
        return a
    else:
        return add_them_up(n, a + 1) + a


n = int(input('Enter a positive number: '))
if n < 1 or n > 10000:
    print('something went wrong')
else: 
    print('The sum is', add_them_up(n, 1))