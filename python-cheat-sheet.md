
# Cheat Sheet for Algorithm - Python

## TOC
- [I/O](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#io)
- [Assignment](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Assignment)
- [Calculations](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Calculations)
- [Condition](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Condition)
- [Loop](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Loop)
- [Function](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Function)
- [String](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#String)
- [List](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#List)
- [Stack](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Stack)
- [Dictionary](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Dictionary)
- [string indexing](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#string-indexing)
- [Type Conversion](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Type-Conversion)
- [OS](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#OS)
- [Pipenv](https://github.com/godori/today-algorithm/blob/master/python-cheat-sheet.md#Pipenv)


## I/O
**[⬆ Top](#toc)**
```python
print('hello world')
input_str = input()
```

## Assignment
**[⬆ Top](#toc)**
```python
test_str = "0 1 2"

# map : a=0, b=1, c=2
a, b, c = map(int, test_str.split())

# arr = [0,1,2]
arr = [int(n) for n in test_str.split()]
```

## Calculations
**[⬆ Top](#toc)**
```python
x**y   # Exponentiation(x^y)

x%y    # Remainder(x%y)

x // y # Division(x/y)

abs(x) # Absolute Value(|x|)
```
- No Prefix/Postfix Operator
```python
i += 1 # i++ or ++i
```

## Condition
**[⬆ Top](#toc)**
```python
name = input()

if name == 'godori':
  print("Hi, godori")
elif name == 'irodog':
  print("Hi, irodog")
else:
  print("Who are you?")
```

- and (&&) or(||)
```python
a = true
b = false
if a == true and b == true:
  print('can not reach here')

if a == true or b == true:
  print('you are here!')
```

## Loop
**[⬆ Top](#toc)**
  ```python
  members = ['godori', 'irodog', 'roodig']

  # for item in items
  for member in members:
    print(member)

  # for idx in range(number)
  for i in range(len(members)):
    print(members[i])

  # enumerate()
  for idx, val in enumerate(arr):
    print(idx, val)
  ```

## Function
**[⬆ Top](#toc)**
- Function call with parameter & return
    ```python
    def func(num):
        return 'godori' * num

    print(func(3))
    ```

- Function string & number parameters
    ```python
    def func(str, num):
        return str * num

    print(func('hey', 3))
    ```

## String
**[⬆ Top](#toc)**
- loop through
  ```python
  str = 'hello'
  for s in str:
    print(s)
  ```

## List
**[⬆ Top](#toc)**
- Length
  ```python
  arr = [1, 2, 3]
  len(arr)
  ```
- Append
  ```python
  arr = [1, 2, 3]
  arr.append(4)
  ```
- Sort
  ```python
  arr = [3, 1, 2]
  arr.sort()
  ```
- Initialize
  ```python
  arr = [0] * 3    # [0,0,0]
  ```
- Reverse
  ```python
  str = "GODORI"
  str[::-1]       # "IRODOG"
  ```
## Stack
**[⬆ Top](#toc)**
- using list like stack
- push
  ```python
  stack = []
  stack.append(1) # add item into the last index
  stack.append(2)
  # stack = [1,2]
  ```
- pop
  ```python
  stack = [1,2,3] # remove tail item
  stack.pop()
  # stack = [1,2]
  ```

## Dictionary
**[⬆ Top](#toc)**
```python
  dic = dict()              # {}
  dic = {}
  
  dic['name'] = 'godori'    # {'name': 'godori'}
  dic['job'] = 'developer'  # {'job':'developer', 'name': 'godori'} (no order)
  print('name' in dic)      # true
  len(dic)                  # 2
```

- Count Frequency of characters in string
```python
   dic = {}
   for c in str:
      if c in dic:
        dic[c] += 1
      else:
        dic[c] = 0
```
## String Indexing
**[⬆ Top](#toc)**
- str[first:last(not inclding)]
```python
  s = "Life is too short, You need Python"
  s[0]     # L
  s[0:3]   # Lif
```

## Type Conversion
**[⬆ Top](#toc)**
- `string` to `int`
  ```python
  int('13')
  ```
  
- `int` to `string`
  ```python
  str(13)
  ```

## OS
**[⬆ Top](#toc)**
- Access environment from python
  ```shell
  $ export OUTPUT_PATH="filename.txt"
  $ echo $OUTPUT_PATH  # filename.txt
  ```
  ```python
  import os

  if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    f.write('write something...')
    f.close()
  ```

## Pipenv
**[⬆ Top](#toc)**
Run pipenv shell

```shell
$ pipenv shell
```
