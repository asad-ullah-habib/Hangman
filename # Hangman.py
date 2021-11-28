import random

# global variables
max_tries = 7
max_errors = 3
user_attempts = 0
list_of_words = 'thr four fivee sixsix sevennn eightttt'.split()
for i in range(len(list_of_words)):  # capitalise all list
    list_of_words[i] = list_of_words[i].upper()
guessed = []  # list of guessed words
list_of_letters =  'First Second Third Fourth Fifth Sixth Seventh Eighth'.split()   # needed for print statement,
# assuming max characters in a word are eight

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
    print('Your word has', len(w), 'letters')
    print('_' * len(w))


def main_program(user_attempts):
    user_tries = user_attempts
    error_counter = 0
    counter_for_letter = 0
    word = list_of_words[random.randint(0, len(list_of_words) - 1)]  # to choose word
    chars_in_word = ['_'] * (len(word))  # used to display the words user got right

    initialise(word)  # program starts

    while user_tries <= max_tries - 1:
        print('Enter your', list_of_letters[counter_for_letter], 'letter: ')  # Taking Input
        user_try = input()

        if len(user_try) == 1 and user_try.isalpha() is True:  # checking input
            user_try = user_try.upper()  # capitalising

            if user_try in word:  # if guess is correct
                print('Correct!')
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

                if word == list_to_string(chars_in_word):  # if user wins
                    print('You won!. Congrats')
                    break

            elif user_try not in word:  # if guess is incorrect
                if user_try in guessed:
                    print('You have already guessed this!')

                else:
                    if user_tries < max_tries - 1:
                        print('Fail! Try Again')
                        print(hangman_stages[user_tries])
                    else:
                        print('You used all your tries. Game Lost!')
                        print(hangman_stages[user_tries])
                    guessed.append(user_try)  # make a list of words user has guessed
                    user_tries += 1

        else:
            print('Value Error. Enter a Valid Value.')
            error_counter += 1
            if error_counter > max_errors:
                print('Too many Errors!. Game over')
                break


main_program(user_attempts)
