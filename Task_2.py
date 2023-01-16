try:

    from random import randint
    lst = [randint(0, 1000) for i in range(30)]
    print(lst)


    if len(lst) == len(set(lst)):
        print('All numbers are unique')
    else:
        print('Unfortunately, not all numbers are unique')

except TypeError:
    print('Check type object')
except NameError:
    print('Check name name object')
# if range value will 100000000 or more
except KeyboardInterrupt:
    print('the program will run for a long time')



