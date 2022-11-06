import random
import words
import ascii_art
# choose random word from the list

chosen_word=random.choice(words.word_list)
display=[]
# guess the letter from the random word

print(f'Solution is {chosen_word}')

for letter in range(len(chosen_word)):
  display+="_"
print(display)

lives=6
life_meter=["1","2","3","4","5"]

end_of_game = False
while not end_of_game:
  guess= input("Guess a letter: ").lower()
  
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position]=letter

  print(display)

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose.")
    else:
      print("No. of Lives You have: "+ life_meter[lives-1])
  
  
  if "_" not in display:
    end_of_game = True
    print("You Win!")
