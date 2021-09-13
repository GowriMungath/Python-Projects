#check if a guessed letter appears in a word
word_list = ["aardvark", "baboon", "camel"]
import random as r
chosen_word=r.choice(word_list)
print(chosen_word)
guess=input("Guess a letter ").lower()
for i in chosen_word:
  if i == guess:
    print("right")
  else:
    print("wrong")
    
#replacing blanks
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display=[]
for i in chosen_word:
  display.append("_")
guess = input("Guess a letter: ").lower()
for i in range(len(chosen_word)-1):
    if chosen_word[i] == guess:
        display[i]=guess;
print(display)
