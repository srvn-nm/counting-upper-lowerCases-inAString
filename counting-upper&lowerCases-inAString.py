# author : Sarvin Nami
def count (word) :
    low = 0
    up = 0
    for item in word :
        if item.islower() :
            low += 1
        elif item.isupper() :
            up += 1
        else :
            pass
    print(f'number of upper case letters : {up}')
    print(f'number of lower case letters : {low}')
name = input('Please enter your name here and if you wanna stop enter # : ')
while name != '#' :
    count(name)
    name = input('Please enter your name here and if you wanna stop enter # : ')