import random

# variables
from typing import List

max_tries = 3
max_errors = 3
list_of_words = ['FIVEE', 'FOUR', 'THR', 'SIXXXX', 'A']
guessed = []  # list of guessed words
list_of_letters = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh',
                   'Eighth']  # needed for print statement


def list_to_string(s):  # helper function( just hide )
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def initialise(word):  # a welcome script. Ignore
    print('Welcome to Hangman!' + '\n' + 'You have', max_tries, 'available lives')
    print('Your word has', len(word), 'letters')
    print('_' * len(word))


def main_program():
    user_tries = 0
    error_counter = 0
    counter_for_letter = 0
    word = list_of_words[random.randint(0, len(list_of_words) - 1)]  # to choose word
    chars_in_word = ['_'] * (len(word)) # used to display the words user got right
    initialise(word) # program starts

    while user_tries <= max_tries - 1:
        print('Enter your', list_of_letters[counter_for_letter], 'letter: ')  # Taking Input
        user_try = input()

        if len(user_try) == 1 and user_try.isalpha() is True:  # checking input
            user_try = user_try.upper()  # capitalising

            if user_try.upper() in word:  # if guess is correct
                print('Correct!')
                counter_for_letter += 1
                func_word = word  # made for use in the for loop below (can be ignored)

                for i in range(len(word)):
                    if func_word.find(user_try.upper()) == -1:  # check if char is not in word
                        break
                    else:
                        chars_in_word.pop(func_word.find(user_try.upper()))  # remove char from list
                        chars_in_word.insert(func_word.find(user_try.upper()), user_try.upper())  # add user_try to list
                        func_word = func_word.replace(user_try.upper(), str(i), 1)  # modify func_word
                print(list_to_string(chars_in_word))  # print letters user got right

                if word == list_to_string(chars_in_word): # if user wins
                    print('You won!. Congrats')
                    break

            elif user_try.upper() not in word:
                if user_try.upper() in guessed:
                    print('You have already guessed this!')

                else:
                    if user_tries < max_tries - 1:
                        print('Fail! Try Again')
                    guessed.append(user_try.upper())  # make a list of words user has guessed
                    user_tries += 1

        else:
            print('Value Error. Enter a Valid Value.')
            error_counter += 1
            if error_counter > max_errors:
                print('Too many Errors!. Game over')
                break


main_program()
