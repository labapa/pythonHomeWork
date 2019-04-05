num = input()
num = int(num)

for i in range (num,-1,-1):
    for j in range(num-i,0,-1):
        print(' ')
    for k in range (0,i*2+1):
        print('*')
    print()
