import random     #library for random used for generating words randomly from a chosen category 
import sys  # sys add time are used in slow_print function; to slowdown the printing speed.
import time

max_errors = 3
number_of_attempts = 0  # added this to fix a bug
guessed = []  # list of guessed words
speed = 0.04 # speed of print statements
word_key_value = ''
list_of_letters = 'First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh ' \
                  'Twelfth Thirteenth Fourteenth Fifteenth  '.split()  # needed for print statements
master_dict = {'Cities Of Pakistan': 'Bahawalpur Swat Chitral Sibi Sukkur Faisalabad Gujrat Jacobabad '.split(),
               'Shows/Series/Movie': 'Lucifer Peaky-Blinders Squid-Game Twilight Money-Heist '
                                     'Annabelle Home-alone Harry-Potter'.split(), 
               'Habib': 'Tariq-Rafi Yohsin-Hall Soorty-Hall Amphitheatre Mehfil Bhaitak Zen-Garden Playground'.split()
               } #dictionary of words which are being split using .split() method which stores each word in a list

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
       # r is for raw string and triple quotes are for printing the hangman excatly as given. This was something we have leaned ourselves.


def choose_a_word(dictionary, key_value): # Choosing the word from the main dictionary randomly
    for k in dictionary:  
        for i in range(len(dictionary[k])):  # capitalise all list
            dictionary[k][i] = dictionary[k][i].upper() # capitalise every value in dictionary
    key_values = list(master_dict)[key_value]
    word_index_value = random.randint(0, len(dictionary[key_values]) - 1)
    return dictionary[key_values][word_index_value]


def slow_print(t): #for printing the message prompt slowly, a new thing we have added ourseleves.
    # https://stackoverflow.com/questions/20302331/typing-effect-in-python
    for i in t:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed)  
    print('')


def list_to_string(s):  # helper function for converting list values into string
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def category_and_word(): # This will let the user choose a category, but word is chosen randomly from that category.
    print('-' * 100) # just for the display it will print a string in the very beginning
    slow_print(
        'Welcome to Hangman! \nYou have 7 tries by default, but you can choose a difficulty level.')
    slow_print('Do you want to choose a category? Press Y for yes and N for no:')
    while True:
        ask = input() 
        if len(ask) == 1 and ask.isalpha() is True:  # checking input
            ask = ask.lower() # all in lower case
            if ask == 'y':
                slow_print(
                        'Choose your category:\n'
                        'Press 1 for Cities Of Pakistan\n'
                        'Press 2 for Shows/Series/Movie\n'
                        'Press 3 for Places in Habib: ')
                for i in range(max_errors + 2):

                    if i < 4:
                        choose = input() 
                        if len(choose) == 1 and choose.isdigit() is True: 
                            if choose == "1":

                                return choose_a_word(master_dict, 0)
                            elif choose == "2":

                                return choose_a_word(master_dict, 1)
                            elif choose == "3":

                                return choose_a_word(master_dict, 2)
                            else:
                                if i != 3:
                                    print('Input Error. Enter a Valid Value.')
                        else:
                            if i != 3:
                                print('Input Error. Enter a Valid Value.')
                    else:
                        print('Too many errors. Random Category Chosen')
                        x = random.randint(0, len(master_dict) - 1) # randomly select category
                        return choose_a_word(master_dict, x)
                

            elif ask == 'n':
                x = random.randint(0, len(master_dict) - 1)
                return choose_a_word(master_dict, x)
            else:
                print('Input Error. Enter a Valid Value.'
                      '\nValue has to be either y or n')
        else:
            print('Input Error. Enter a Valid Value.'
                  '\nValue has to be either y or n')


def difficulty(): # let user choose a difficulty level 
    while True:
        slow_print('Do you want to choose a difficulty level? Press Y for yes press and N for no')
        ask = input()
        if len(ask) == 1 and ask.isalpha() is True:  # checking input
            ask = ask.lower()
            if ask == 'y':
                slow_print(
                    'Choose your difficulty:\n'
                    'Press 1 for Easy (guess the word(s) in 7 tries)\n'  # easy means all 7 tries
                    'Press 2 for Medium (guess the word(s) in 5 tries)\n'  # medium means 5 tries to guess the word
                    'Press 3 for Hard(guess the word(s) in 3 tries) ')  # hard means only 3 chances will be given for guessing the word
                for i in range(max_errors + 2):
                    if i < 4:
                        hangman_difficulty = input()
                        if len(hangman_difficulty) == 1 and hangman_difficulty.isdigit() is True :
                            if hangman_difficulty == '1':
                                return 7
                            elif hangman_difficulty == '2':
                                return 5
                            elif hangman_difficulty == '3':
                                return 3
                        else:
                            print('Input Error. Value has to be between 1 and 3')
                    else:
                        print('Input Error. Value has to be between 1 and 3')
                print('Too many wrong inputs. Easy Level selected')
                return 7

            elif ask == 'n':
                return 7 # this is the number of user tries 
            else:
                print('Input Error. Enter a Valid Value.'
                      '\nValue has to be either y or n')
        else:
            print('Input Error. Enter a Valid Value.'
                  '\nValue has to be either y or n')


def main_program(user_tries, word):
    error_counter = 0
    counter_for_letter = 0
    max_tries = difficulty()  # added 'difficulty' for choosing a difficulty level

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
                temp_word = word  # made for use in the for loop below 
                for u in range(len(word)):
                    if temp_word.find(user_try) == -1:  # check if char is not in word
                        break
                    else:
                        
                        chars_in_word.pop(temp_word.find(user_try))  # remove char from list
                        chars_in_word.insert(temp_word.find(user_try.upper()), user_try)  # add user_try to list
                        temp_word = temp_word.replace(user_try, str(u), 1)  # modify temp_word
                slow_print(str(list_to_string(chars_in_word)))  # print letters user got right

                if word.replace('-', ' ') == list_to_string(chars_in_word):  # if user wins. print win statement
                    slow_print('You won!. Congratulations!!!! \nHave a chocolate.')
                    time.sleep(1)  # Slow down program, 1 sec pause then program ends
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
                        print("You have", max_tries - user_tries, "tries left!") #displays how many tries are left after each incorrect word guessed


                    else:
                        slow_print('You have used up all your tries, sorry.'
                                   '\nGame Lost!')
                        slow_print('The correct word(s) was:')
                        slow_print(generated_word.replace("-", " ")) # from the words in the end while displaying the generated word if incorrectly guessed.
                        break


        else:
            print('InputError. Enter a Valid Value.'
                       '\nValue has to be a single character from the English Alphabet')
            error_counter += 1
            if error_counter > max_errors:
                slow_print('Too many Input Errors!.\n'
                           'Game over!') #when there are too many incorrect inputs program ends
                break
    

generated_word = category_and_word() 
main_program(number_of_attempts, generated_word)