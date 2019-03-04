
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

