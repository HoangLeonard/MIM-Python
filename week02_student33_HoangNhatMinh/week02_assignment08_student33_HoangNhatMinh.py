# Half Pyramid
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print("_____________")
# Inverted Half Pyramid
print('******')
print('*****')
print('****')
print('***')
print('**')
print('*')
print("_____________")
# Hollow Inverted Half Pyramid
for i in range(1,7) :
    for j in range(1,7) :
        if ( i==1 or j==1 ) :
            print('*', end='')
        elif (7-i == j) :
            print('*', end='')
        else : print(end=' ')
    print()
print("_____________")
# Full Pyramid
for i in range(0,7) :
    for j in range(0,13) :
        check1 = j >= -i + 6
        check2 = j <= i + 6
        if  check2 and check1 :
            print(end='*')
        else : print(end=' ')
    print()
print("_____________")
# Inverted Full Pyramid
for i in range(0,7) :
    for j in range(0,13) :
        check1 = j >= i
        check2 = j <= -i + 12
        if  check2 and check1:
            print(end='*')
        else : print(end=' ')
    print()
print("_____________")
# Hollow Full Pyramid
for i in range(0,7) :
    for j in range(0,13) :
        check1 = j == -i + 6
        check2 = j == i + 6
        check3 = i == 6
        if  check2 or check1 or check3 :
            print(end='*')
        else : print(end=' ')
    print()
print("_____________")