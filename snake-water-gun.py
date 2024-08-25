import random
print("Welcome to SNAKE WATER GUN\n")
i=0
pscore=0
cscore=0
choices=1,2,3
while True:
    i+=1
    try:
         p=int(input('Choose 1 for snake , 2 for water and 3 for gun'))
         c=random.choice(choices)
    except ValueError:
    
        print("Invalid choice! Please Choose 1 for snake , 2 for water and 3 for gun.")
        continue
    if p==c:
        print('Tie')
    elif p == 1 :
        if c==2:
            print("You win! Snake drank water.")
            pscore+=1
        else:
            print("ooops, You lost")
            cscore+=1
    elif p == 2 :
        if c==3:
            print("You win!")
            pscore+=1
        else:
            print("ooops, You lost")
            cscore+=1
    elif p == 3 :
        if c==1:
            print("You win!")
            pscore+=1
        else:
            print("ooops, You lost")
            cscore+=1
    print(f'Your score = {pscore} and Computer score ={cscore}' )
    if i==10:
            print("Game over ")        
            break
print(f'Your Final score is {pscore} and Computer Final score is {cscore}' )

if pscore > cscore:
        print("VICTORY")
else:
    print("HARD LUCK")
print('Thanks for playing')



