def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    t = 0
    while (x1 + v1 * t) <= (x2 + v2 * t):
        if (x1 + v1 * t) == (x2 + v2 * t):
            return "YES"
        t += 1
    return "NO"


if __name__ == '__main__':
    arr = [int(n) for n in input().split()]
    print(kangaroo(arr[0], arr[1], arr[2], arr[3]))
