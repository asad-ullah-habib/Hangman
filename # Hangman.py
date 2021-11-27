import random

# variables
max_tries = 3
list_of_words = ['FIVEE', 'FOUR', 'THR', 'SIXXXX', 'A']
tries = 0
word = list_of_words[random.randint(0, len(list_of_words) - 1)]  # to choose word
chars_in_word = ['_'] * (len(word))
guessed = []  # list of guessed words
max_errors = 3


def list_to_string(s):  # helper function
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def initialise():
    print('Welcome to Hangman!' + '\n' + 'You have', max_tries, 'available lives')
    print('Your word has', len(word), 'letters')
    print('_' * len(word))


def main_program():
    user_tries = 0
    error_counter = 0
    initialise()

    while user_tries <= max_tries - 1:

        user_try = input('Enter your first Letter: ')  # Taking Input

        if len(user_try) == 1 and user_try.isalpha() is True:  # checking input
            user_try = user_try.upper()  # capitalising

            if user_try.upper() in word:  # if guess is correct
                print('Sucess')
                

                # need to add code to handle multiple instances of the same character #

                chars_in_word.pop(word.find(user_try.upper()))
                chars_in_word.insert(word.find(user_try.upper()), user_try.upper())
                print(list_to_string(chars_in_word))

                if word == list_to_string(chars_in_word):
                    print('You won!. Congrats')
                    break

            elif user_try.upper() not in word:
                if user_try.upper() in guessed:
                    print('You have already guessed this!')

                else:
                    if user_tries < max_tries - 1:
                        print('Fail! Try Again')
                    guessed.append(user_try.upper())
                    user_tries += 1

            elif len(word) == len(chars_in_word):
                print('You won!')
                break

            elif error_counter > max_errors:
                print('Game Over')
                break

        else:
            print('Value Error. Enter a Valid Value.')
            error_counter += 1

            if error_counter > max_errors:
                print('Too many Errors!. Game over')
                break
    # print('You lost!')


main_program()
