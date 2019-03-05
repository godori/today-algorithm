import os
import sys


def gradingStudents(grades):
    for i, v in enumerate(grades):
        n = (v // 5 + 1) * 5
        if v < 38:
            continue
        if abs(v - n) < 3:
            grades[i] = n
    return (grades)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()