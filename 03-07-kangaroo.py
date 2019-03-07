def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    t = 0
    while 1:
        p1 = x1 + v1 * t
        p2 = x2 + v2 * t
        if p1 == p2:
            return "YES"
        elif p1 > p2:
            return "NO"
        t += 1
    return "NO"


if __name__ == '__main__':
    arr = [int(n) for n in input().split()]
    print(kangaroo(arr[0], arr[1], arr[2], arr[3]))
