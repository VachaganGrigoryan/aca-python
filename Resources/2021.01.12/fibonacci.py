def fibonacci():
    a, b = 1, 1
    while True:
        cmd = yield b
        if cmd == 'reset':
            a, b = 1, 1
            continue
        a, b = b, a + b


if __name__ == '__main__':
    f = fibonacci()
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(f.send('reset'))
    print(next(f))
    print(next(f))
    
