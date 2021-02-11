def move(n, source='A', target='B', aux='C'):
    if n == 0:
        return
    move(n - 1, source, aux, target)
    move(n - 1, aux, target, source)

if __name__ == '__main__':
    n = int(input())
    move(n)
