def foo(a, b):
    return 'result: ' + str(a + b)


def bar(a, b):
    return '[bar]:result: ' + str(a * b)


if __name__ == '__main__':
    print foo(5, 6)
    print bar(8, 9)
