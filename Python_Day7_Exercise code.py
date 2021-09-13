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
