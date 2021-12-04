import os
import random
import sys
import time

# global variables
max_errors = 3
number_of_attempts = 0  # added this to fix a bug
guessed = []  # list of guessed words
clear = "\n" * 100  # may remove this. Used to clear console
speed = 0.05  # speed of print statements
word_key_value = ''
list_of_letters = 'First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth'.split()  # needed for print
master_dict = {'Cities Of Pakistan': 'Multan Karachi Islamabad Rawalpindi Hyderabad '.split(),  # dictionary of words
               'Flavours of Ice-cream': 'Vanilla chocolate strawberry blueberry  '.split(),
               'Objects': 'table chair bag book dustbin door'.split()
               }
hangman_stages = [r'''
   +---+
       |
       |
       |
      === ''', r'''
   +---+
   O   |
       |
       |
      ===''', r'''
   +---+
   O   |
   |   |
       |
      ===''', r'''
   +---+
   O   |
  /|   |
       |
      ===''', r'''
   +---+
   O   |
  /|\  |
       |
      ===''', r'''
   +---+
   O   |
  /|\  |
  /    |
      ===''', r'''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']


# pictionary of hangman (minimised)


def cls():  # also used to clear console
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_a_word(dictionary):
    for k in dictionary:  # capitalise every value in dictionary
        for i in range(len(dictionary[k])):  # capitalise all list
            dictionary[k][i] = dictionary[k][i].upper()

    # to choose a random key(category) and value(word within that category)
    global word_key_value
    word_key_value = random.choice(list(dictionary.keys()))
    word_index_value = random.randint(0, len(dictionary[word_key_value]) - 1)
    return dictionary[word_key_value][word_index_value]


def slow_print(t):
    for i in t:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed)  # change later #
    print('')


def list_to_string(s):  # helper function( just hide )
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def initialise(w):  # a welcome script. Ignore
    print('-' * 100)
    slow_print('Welcome to Hangman! \nYou have 7 available lives by default.')
    slow_print('Your word has ' + str(len(w)) + ' letters\nYour word is in the category: ' + str(word_key_value))
    slow_print('_' * len(w))


def difficulty():
    while True:
        slow_print('Do you want to choose a difficulty level? [y/n]')
        ask = input()
        if len(ask) == 1 and ask.isalpha() is True:  # checking input
            ask = ask.lower()
            if ask == 'y':
                for i in range(max_errors + 1):
                    slow_print('Choose your difficulty: Easy[ 1 ], Medium[ 2 ] or Hard [ 3 ]: ')
                    hangman_difficulty = input()
                    if len(hangman_difficulty) == 1 and hangman_difficulty.isnumeric() is True:
                        if hangman_difficulty == '1':
                            return 7
                        elif hangman_difficulty == '2':
                            return 5
                        elif hangman_difficulty == '3':
                            return 3
                    else:
                        print('Input Error. Enter a Valid Value.')

            elif ask == 'n':
                return 7

        else:
            print('Input Error. Enter a Valid Value.'
                  '\nValue has to be either y or n')


def main_program(user_tries, word, difficulty_level):
    error_counter = 0
    counter_for_letter = 0
    max_tries = difficulty_level
    while user_tries <= max_tries - 1:
        slow_print('Try to guess your ' + str(list_of_letters[counter_for_letter]) + ' letter: ')
        user_try = input()

        if len(user_try) == 1 and user_try.isalpha() is True:  # checking input
            user_try = user_try.upper()  # capitalising

            if user_try in word and user_try not in guessed:  # if guess is correct
                slow_print('You are Correct!')
                counter_for_letter += 1
                func_word = word  # made for use in the for loop below (can be ignored)

                for u in range(len(word)):
                    if func_word.find(user_try) == -1:  # check if char is not in word
                        break
                    else:
                        chars_in_word.pop(func_word.find(user_try))  # remove char from list
                        chars_in_word.insert(func_word.find(user_try.upper()), user_try)  # add user_try to list
                        func_word = func_word.replace(user_try, str(u), 1)  # modify func_word
                slow_print(str(list_to_string(chars_in_word)))  # print letters user got right

                if word == list_to_string(chars_in_word):  # if user wins. print win statement
                    slow_print('You won!. Congratulations!!!! \nHave a chocolate.')
                    break

            elif user_try not in word:  # if guess is incorrect
                if user_try in guessed:
                    slow_print('You have already guessed this!\nTry again.')

                else:
                    if user_tries < max_tries - 1:
                        slow_print('Your guess is incorrect.\nTry Again')
                        slow_print(hangman_stages[user_tries])
                        slow_print(str(list_to_string(chars_in_word)))

                    else:
                        slow_print('You have used up all your tries, sorry.'
                                   '\nGame Lost!')
                        print(hangman_stages[user_tries])
                    guessed.append(user_try)  # make a list of words user has guessed
                    user_tries += 1

        else:
            slow_print('Input Error. Enter a Valid Value.'
                       '\nValue has to be a single character from the English Alphabet')
            error_counter += 1
            if error_counter > max_errors:
                slow_print('Too many Input Errors!.\nYou get to shit over my program 3 times.'
                           '\nYou have successfully done that. Game over!')
                break


generated_word = choose_a_word(master_dict)
chars_in_word = ['_'] * (len(generated_word))  # used to display the words user got right
initialise(generated_word)  # program starts
main_program(number_of_attempts, generated_word, difficulty())  # while loop
