# MODULES
import random

# DEFINING THE NUMBER OF LIFES
life = 6

# ASCII ART

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# MAKING A RANDOM WORD
# METHOD 1 COMPLETELY RANDOM WORDS
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# word = ""

# word_length = random.randint(5, 10)

# for i in range(word_length):
#     letter = random.choice(letters)
#     word += letter

# METHOD 2 WORDS OF A LIST

words = ['sai', 'varshith', 'aalasyam', 'bollam',
         'pravalika', 'ram', 'sunil', 'kumar', 'reddy', 'gudapureddy']
# words = ['oooooooooooo']

word = random.choice(words)
word_length = len(word)

# MAKING SPACES BETWEEN THE WORD
spaces = random.randint(1, word_length)
# print(spaces)

space = []
for i in range(spaces):
    s = random.randint(1, word_length)
    space.append(s)


# MAKING THE WORD THAT WILL BE DISPLAYED ON SCREEN
display_word = []

# CHECKS IF THE NUMBER IS PRESENT IN SPACES NEEDED LIST OR NOT


def exists_in_space(a):
    for i in space:
        if i == a:
            return True
        else:
            continue
    return False


for i in range(word_length):
    display_word.append("-")
# s = 0
for i in range(word_length):
    if exists_in_space(i):
        display_word[i] = "_"
        # s += 1
    else:
        display_word[i] = word[i]


def list_to_str(list):
    DISPLAY = ""
    for i in range(len(list)):
        DISPLAY += list[i]
    return DISPLAY


# MAKING A LIST OF NOT DISPLAYED LETTERS FOR CHECKING THE GUESS
not_display = []

for i in range(len(word)):
    if word[i] == display_word[i]:
        continue
    else:
        # not_display += word[i]
        not_display.append(word[i])
# print(not_display)

# CHECKING IF THE GUESS IS CORRECT OR NOT


def check_guess(guess):
    for i in not_display:
        if guess == i:
            global s
            s -= 1
            a = word.index(i)
            display_word[a] = i
            # not_display.replace(guess, "")
            not_display.remove(guess)
            print(not_display)
            return True
        else:
            continue
    return False


print(logo)

s = len(not_display)

while (life > 0) and (s > 0):
    print(f"The half word is {list_to_str(display_word)}")
    guess = input("Enter your letter guess: ")
    result = check_guess(guess)
    if not result:
        life -= 1
        print(stages[life])
        print(f"lifes left are {life}")

if life == 0:
    print("You are dead")
    print(f"The word is {word}")
else:
    print("You Won")
