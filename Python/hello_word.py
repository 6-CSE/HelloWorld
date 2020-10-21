from random import randint
hw = ['o', 'l', 'w', 'l', 'e', 'h', 'l', 'r', 'd']

count = 0
while True:
    count += 1
    result = f'{hw[randint(0, 8)]}{hw[randint(0, 8)]}{hw[randint(0, 8)]}{hw[randint(0, 8)]} {hw[randint(0, 8)]}{hw[randint(0, 8)]}{hw[randint(0, 8)]}{hw[randint(0, 8)]}{hw[randint(0, 8)]}'
    print(result)
    if result == 'hello world':
        print(f'{count} attempts until the result')
        break
