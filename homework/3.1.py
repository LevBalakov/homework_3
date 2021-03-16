def div(*args):
    try:
        arg1 = int(input("Число 1: "))
        arg2 = int(input("Число 2: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return res
print(f'result  {div()}')