# Today's algorithm
if __name__ == '__main__':
    res = []
    q = int(input().strip())
    for _ in range(q):
        x,y,z = (int(n) for n in input().strip().split())
        if abs(x-z) == abs(y-z):
            res.append('Mouse C')
        elif abs(x-z) < abs(y-z):
            res.append('Cat A')
        else:
            res.append('Cat B')
    for _ in res:
        print(_)