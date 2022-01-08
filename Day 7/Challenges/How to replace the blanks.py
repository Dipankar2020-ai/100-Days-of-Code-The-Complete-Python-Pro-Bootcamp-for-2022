import random
word_list=["andvark","baboon","camel"]
chosen_word=random.choice(word_list)
length=len(chosen_word)
guess=input("Guess a letter : ").lower()
display=[]
for i in chosen_word:
    display+="_"

for position in range(length):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter
print(display)
