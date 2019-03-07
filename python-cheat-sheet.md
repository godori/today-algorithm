
# Cheat Sheet for Algorithm - Python

## Output
```python
print('hello world')
```

## Input
```python
input_str = input()

# "0 1 2" -> arr = [0,1,2]
arr = [int(n) for n in input().split()]
```


## Calculations

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
```python
name = input()

if name == 'godori':
  print("Hello, godori")
elif name == 'irodog':
  print("Hello, irodog")
else:
  print("Who are you?")
```

## Loop

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

## List
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

## OS
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

Run pipenv shell

```shell
$ pipenv shell
```
