dic = [0, 0, 0, 0, 0]

if __name__ == '__main__':
    cnt = input()
    arr = [int(n) for n in input().split()]

    for v in arr:
        dic[(v-1]=dic[v-1] + 1

    max=dic[0]
    res=1
    for i in range(1, len(dic)):
        if max < dic[i]:
            max=dic[i]
            res=i+1

    for i in range(1, len(dic)):
        if max < dic[i]:
            max=dic[i]
            res=i+1

    print(res)
