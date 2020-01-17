# roll the dice program


import random
# name
print('what is your name?')
name = input()

# introduction
print('well hello there ' + name + ', would you like to roll the dice?')
answer = None
while answer not in ('yes', 'no'):
    answer = input('yes or no: ')
    if answer == 'yes':
        print('ok, we will now begin')
    elif answer == 'no':
        print('move along traveller')
        exit()
    else:
        print('you are testing me. enter yes or no.')

# di selection
print('i have 3 types of di, you choose')
answer = None
while answer not in ('D6', 'D12', 'D20'):
    answer = input('would you like to play with D6, D12 or D20?: ')
# D6
    if answer == 'D6':
        print('ok')
        print('my turn first')
        myGo = random.randint(1,6)
        print('i got ' + str(myGo) + ' your turn')
        print('roll.')
        answer = None
        while answer not in ('yes', 'no'):
            answer = input('yes or no: ')
            if answer == 'yes':
                yourGo = random.randint(1,6)
                print('you got ' + str(yourGo) + '!')
                while True:
                    if yourGo > myGo:
                        print('you win ' + name)
                        break
                    if yourGo < myGo:
                        print('you lose')
                        break
                    if yourGo == myGo:
                        print('its a tie')
                        break
            elif answer == 'no':
                print('chicken')
                exit()
            else:
                print('you are testing me. enter yes or no.')      
#D12          
    elif answer == 'D12':
        print('ok')
        print('my turn first')
        myGo = random.randint(1,12)
        print('i got ' + str(myGo) + ' your turn')
        print('roll.')
        answer = None
        while answer not in ('yes', 'no'):
            answer = input('yes or no: ')
            if answer == 'yes':
                yourGo = random.randint(1,12)
                print('you got ' + str(yourGo) + '!')
                while True:
                    if yourGo > myGo:
                        print('you win ' + name)
                        break
                    if yourGo < myGo:
                        print('you lose')
                        break
                    if yourGo == myGo:
                        print('its a tie')
                        break
            elif answer == 'no':
                print('chicken')
                exit()
            else:
                print('you are testing me. enter yes or no.')
#D20
    elif answer == 'D20':
        print('oh, my favourite')
        print('my turn first')
        myGo = random.randint(1,20)
        print('i got ' + str(myGo) + ' your turn')
        print('roll.')
        answer = None
        while answer not in ('yes', 'no'):
            answer = input('yes or no: ')
            if answer == 'yes':
                yourGo = random.randint(1,20)
                print('you got ' + str(yourGo) + '!')
                while True:
                    if yourGo > myGo:
                        print('you win' + name)
                        break
                    if yourGo < myGo:
                        print('you lose')
                        break
                    if yourGo == myGo:
                        print('its a tie')
                        break
            elif answer == 'no':
                print('chicken')
                exit()
            else:
                print('you are testing me. enter yes or no.')
# if they dont answer right  
    else:
        print('that is not a valid di.')





