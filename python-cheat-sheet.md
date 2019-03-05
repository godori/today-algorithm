
# Cheat Sheet for Algorithm - Python

## Output
```python
print('hello world')
```

## Input
```python
input_str = input()
```

## Condition
```python
name = input()

if name == 'godori':
  print("Hello!, godori")
elif name == 'irodog':
  print("Hello!, irodog")
else:
  print("Who are you?")
```

## Loop
- for...in
    ```python
    members = ['godori', 'irodog', 'roodig']

    for member in members:
      print(member)

    for anything in range(3):
      print('yo')

    for _ in range(len(members)):
      print(members[_])
    ```
## Function

- Function call with parameter & return
    ```python
    def func(num):
        return 'hello' * num

    print(func(3))
    ```

- Function string & number parameters
    ```python
    def func(str, num):
        return str * num

    print(func('hey', 3))
    ```

## List
- List length
  ```python
  arr = [1, 2, 3]
  len(arr)
  ```
- List sort
  ```python
  arr = ['c','a','b']
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
