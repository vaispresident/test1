def sum_all(a):
    count = 0
    for i in range(1,a+1):
        count+=i
    return count

    # while count!=a:
a=int(input('enter number: '))
print(sum_all(a))