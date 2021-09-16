
#hangman.py
print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                           """)  




list=(""" _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / \\
     |
     |
     |___""", """ _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / 
     |
     |___""",""" _______
     |/      |
     |       O
     |      \|/
     |       |
     |      
     |
     |___""",""" _______
     |/      |
     |       O
     |      \|/
     |       
     |      
     |
     |___""",""" _______
     |/      |
     |       O
     |      \|
     |       
     |    
     |
     |___""",""" _______
     |/      |
     |       O
     |      \\
     |       
     | 
     |
     |___""",""" _______
     |/      |
     |       O
     |      
     |       
     |      
     |
     |___""")    


import word_dict as w
total_lives=7
import random
chosen_word=random.choice(w.word_list)
display=[]
for i in chosen_word:
    display.append("_")

already=[]
while(total_lives>0):
        al=0
        p=0
        guess = input("Guess a letter: ").lower()
        for i in already:
            if i==guess:
                print("You already guessed this letter. Go for another one!")
                al=1
                break
        if not al==1:
            already.append(guess)
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i]=guess
                    p=1
            print(display)
            if p==0:
                total_lives-=1
                print(list[total_lives])
            for j in display:
                if j=='_':
                    a=0
                    break
                else:
                    a=1
            if a==1:
                print("You win")
                exit(0)
if total_lives<=0:
    print("You lose! Game Over!")
    print(chosen_word)
