import random
import time
num = random.randint(0, 100)
answer = 'Y'
while answer == 'Y':
    yuyu = False
    while yuyu == False:
        guess = int(input('guess number between 1-100: '))
        
        if guess == num:
            print('correct')
            time.sleep(1)
            
            answer = input('play again? [y : n]: ')
            answer.upper()
            if answer == 'Y':
                yuyu == False
            else:
                yuyu = True
                quit()
            
            
        
        if guess != num and guess <= num:
            print('HIGHER!!!')
        if guess != num and guess >= num:
            print('LOWER!!!')
            


