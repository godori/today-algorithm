# n = steps
# U uphill
# D downhill

# find valley number
# valley = starts step down from sea lv ending with a step up sea lv
# _/\       _ ....-> sea level
#    \     /
#     \/\/

if __name__ == "__main__":
    s = v = 0
    step = int(input())
    str = input()

    for idx,val in enumerate(str):
        if val == "D":
            s = s-1
        if val == "U":
            s = s+1
        if idx > 0 and s == 0 and val == 'U':
            v = v+1
    print(v)

