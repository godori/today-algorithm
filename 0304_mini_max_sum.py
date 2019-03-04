def miniMaxSum(arr):
    sum = min = max = 0
    for a in arr:
        sum += a

    min = max = sum - arr[0]

    for b in arr:
        msum = sum - b
        if msum < min:
            min = msum
        if msum > max:
            max = msum

    return print(min, max)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)