import random
import sys
import time
#HEllO THIS IS A TEST
#Hi asad
# global variables
max_errors = 3
number_of_attempts = 0  # added this to fix a bug
guessed = []  # list of guessed words
# clear = "\n" * 100  # may remove this. Used to clear console
speed = 0.09  # speed of print statements
word_key_value = ''
list_of_letters = 'First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh ' \
                  'Twelfth Thirteenth Fourteenth Fifteenth  '.split()  # needed for print
master_dict = {'Cities Of Pakistan': 'Bahawalpur Swat Chitral Sibi Sukkur Faisalabad Gujrat Jacobabad '.split(),
               # dictionary of words
               'Shows/Series/Movie': 'Lucifer Peaky-Blinders Squid-Game Twilight Money-Heist '
                                     'Annabelle Home-alone Harry-Potter'.split(),
               'Habib': 'Tariq-Rafi Yohsin-Hall Soorty-Hall Amphitheatre Mehfil Bhaitak Zen-Garden Playground'.split()
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


def choose_a_word(dictionary, key_value):
    for k in dictionary:  # capitalise every value in dictionary
        for i in range(len(dictionary[k])):  # capitalise all list
            dictionary[k][i] = dictionary[k][i].upper()
    key_values = list(master_dict)[key_value]
    word_index_value = random.randint(0, len(dictionary[key_values]) - 1)
    return dictionary[key_values][word_index_value]


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


def category_and_word():
    while True:
        print('-' * 75)
        slow_print(
            'Welcome to Hangman! \nYou have 7 tries by default, but the tries will change if you would like to choose a difficulty level later on in the game.')
        slow_print('Do you want to choose a category? Press Y for yes and N for no:')
        ask = input()
        if len(ask) == 1 and ask.isalpha() is True:  # checking input
            ask = ask.lower()

            if ask == 'y':
                for i in range(max_errors + 1):
                    slow_print(
                        'Choose your category:\n'
                        'Press 1 for Cities Of Pakistan\n'
                        'Press 2 for Shows/Series/Movie\n'
                        'Press 3 for Places in Habib: ')
                    choose = input()
                    if len(choose) == 1 and choose.isnumeric() is True:
                        if choose == "1":

                            return choose_a_word(master_dict, 0)
                        elif choose == "2":

                            return choose_a_word(master_dict, 1)
                        elif choose == "3":

                            return choose_a_word(master_dict, 2)
                        else:
                            print('Input Error. Enter a Valid Value.')
                    else:
                        print('Input Error. Enter a Valid Value.')

            elif ask == 'n':
                x = random.randint(0, len(master_dict) - 1)
                return choose_a_word(master_dict, x)
        else:
            print('Input Error. Enter a Valid Value.'
                  '\nValue has to be either y or n')


def difficulty():
    while True:
        slow_print('Do you want to choose a difficulty level? Press Y for yes press and N for no')
        ask = input()
        if len(ask) == 1 and ask.isalpha() is True:  # checking input
            ask = ask.lower()
            if ask == 'y':
                for i in range(max_errors + 1):
                    slow_print(
                        'Choose your difficulty:\n'
                        'Press 1 for Easy (guess the word(s) in 7 tries)\n'
                        'Press 2 for Medium (guess the word(s)  in 5 tries)\n'
                        'Press 3 for Hard( guess the word(s) in 3 tries) ')

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


def main_program(user_tries, word):
    error_counter = 0
    counter_for_letter = 0
    max_tries = difficulty()  # added 'difficulty'

    chars_in_word = []
    if generated_word.find('-') == -1:
        chars_in_word.extend(['_'] * (len(generated_word)))  # used to display the words user got right
    else:
        for i in range(len(generated_word)):
            if generated_word[i] == '-':
                chars_in_word.extend(' ')
            else:
                chars_in_word.extend('_')

    if word.find('-') == -1:
        slow_print('Your word has ' + str(len(word)) + ' letters.')
    else:
        slow_print('Your word has ' + str(len(word) - 1) + ' letters.')

    slow_print(str(list_to_string(chars_in_word)))

    while user_tries <= max_tries - 1:
        slow_print('Try to guess your ' + str(list_of_letters[counter_for_letter]) + ' letter: ')

        user_try = input()

        if len(user_try) == 1 and user_try.isalpha() is True:  # checking input
            user_try = user_try.upper()  # capitalising

            if user_try in word and user_try not in guessed:  # if guess is correct
                slow_print('You are Correct!')
                counter_for_letter += 1
                guessed.append(user_try)
                func_word = word  # made for use in the for loop below (can be ignored)
                for u in range(len(word)):
                    if func_word.find(user_try) == -1:  # check if char is not in word
                        break
                    else:
                        chars_in_word.pop(func_word.find(user_try))  # remove char from list
                        chars_in_word.insert(func_word.find(user_try.upper()), user_try)  # add user_try to list
                        func_word = func_word.replace(user_try, str(u), 1)  # modify func_word
                slow_print(str(list_to_string(chars_in_word)))  # print letters user got right

                if word.replace('-', ' ') == list_to_string(chars_in_word):  # if user wins. print win statement
                    slow_print('You won!. Congratulations!!!! \nHave a chocolate.')
                    time.sleep(2)  # Slow down program
                    break

            else:  # if guess is incorrect
                if user_try in guessed:
                    slow_print('You have already guessed this!')

                else:
                    if user_tries < max_tries - 1:
                        slow_print('Your guess is incorrect.\nTry Again')
                        print(hangman_stages[user_tries])
                        slow_print(str(list_to_string(chars_in_word)))
                        guessed.append(user_try)  # make a list of words user has guessed
                        user_tries += 1
                        print("You have", max_tries - user_tries, "tries left!")


                    else:
                        slow_print('You have used up all your tries, sorry.'
                                   '\nGame Lost!')
                        slow_print('The correct word(s) was:')
                        slow_print(generated_word)
                        break


        else:
            slow_print('Input Error. Enter a Valid Value.'
                       '\nValue has to be a single character from the English Alphabet')
            error_counter += 1
            if error_counter > max_errors:
                slow_print('Too many Input Errors!.\n'
                           'Game over!')
                break


generated_word = category_and_word()
main_program(number_of_attempts, generated_word)