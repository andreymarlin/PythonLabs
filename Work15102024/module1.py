def f1(a, b):
    if b == 0:
        return 'Division by zero.'
    else:
        return a/b

def f2(a, b):
    if b == 0:
        b = float('inf')
    return a/b