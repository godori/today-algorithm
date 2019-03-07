def kangaroo(x1, v1, x2, v2):
    if (v1 - v2) <= 0:
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    arr = [int(n) for n in input().split()]
    print(kangaroo(arr[0], arr[1], arr[2], arr[3]))
