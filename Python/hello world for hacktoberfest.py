import time

list_1 = ['H','e','l','l','o']
list_2 = ['W','o','r','l','d']

for i in range(5):
    for x in list_1:
        print(x,end='')
        time.sleep(0.5)
    print(' ')
    for y in list_2:
        print(y,end='')
        time.sleep(0.5)
    print('\n')

    
