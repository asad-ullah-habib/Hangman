import random

# global variables
max_tries = 7
max_errors = 3
number_of_attempts = 0  # added this to fix a bug
guessed = []  # list of guessed words
list_of_letters = 'First Second Third Fourth Fifth Sixth Seventh Eighth'.split()   # needed for print statement,....
# assuming max characters in a word are eight

master_dict = {'Places': 'Multan Karachi Islamabad Rawalpindi Hyderabad '.split(),  # dictionary of words(tentative)
               'Flavours': 'Vanilla chocolate strawberry berry'.split()
               }
for k in master_dict:  # capitalise every value in dictionary
    for i in range(len(master_dict[k])):  # capitalise all list
        master_dict[k][i] = master_dict[k][i].upper()

# to choose a random key(category) and value(word within that category)
word_key_value = random.choice(list(master_dict.keys()))
word_index_value = random.randint(0, len(master_dict[word_key_value]) - 1)
generated_word = master_dict[word_key_value][word_index_value]

# pictionary of hangman
hangman_stages = ['''
   +---+
       |
       |
       |
      === ''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']


def list_to_string(s):  # helper function( just hide )
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def initialise(w):  # a welcome script. Ignore
    print('Welcome to Hangman! You have', max_tries, 'available lives. Use them wisely 😄')
    print('Your word has', len(w), 'letters\nYour word is in the category:', word_key_value)
    print('_' * len(w))


def main_program(user_tries, word):

    error_counter = 0
    counter_for_letter = 0
    chars_in_word = ['_'] * (len(word))  # used to display the words user got right

    initialise(word)  # program starts

    while user_tries <= max_tries - 1:
        print('Try to guess your', list_of_letters[counter_for_letter], 'letter: ')  # Taking Input
        user_try = input()

        if len(user_try) == 1 and user_try.isalpha() is True:  # checking input
            user_try = user_try.upper()  # capitalising

            if user_try in word:  # if guess is correct
                print('You are Correct!')
                counter_for_letter += 1
                func_word = word  # made for use in the for loop below (can be ignored)

                for u in range(len(word)):
                    if func_word.find(user_try) == -1:  # check if char is not in word
                        break
                    else:
                        chars_in_word.pop(func_word.find(user_try))  # remove char from list
                        chars_in_word.insert(func_word.find(user_try.upper()), user_try)  # add user_try to list
                        func_word = func_word.replace(user_try, str(u), 1)  # modify func_word
                print(list_to_string(chars_in_word))  # print letters user got right

                if word == list_to_string(chars_in_word):  # if user wins. print win statement
                    print('You won!. Congratulations!!!!')
                    break

            elif user_try not in word:  # if guess is incorrect
                if user_try in guessed:
                    print('You have already guessed this!\nTry again.')

                else:
                    if user_tries < max_tries - 1:
                        print('Your guess is incorrect.\n Try Again')
                        print(hangman_stages[user_tries])
                    else:
                        print('You have used up all your tries, sorry.'
                              '\nGame Lost!')
                        print(hangman_stages[user_tries])
                    guessed.append(user_try)  # make a list of words user has guessed
                    user_tries += 1

        else:
            print('Input Error. Enter a Valid Value.'
                  '\nValue has to be a single character from the English Alphabet')
            error_counter += 1
            if error_counter > max_errors:
                print('Too many Input Errors!. Game over')
                break


main_program(number_of_attempts , generated_word)
