import random
import re


class Hangman:

    def __init__(self):
        self.dic_words = 'python', 'java', 'swift', 'javascript'
        self.win_num = 0
        self.lose_num = 0
        self.current_stage = 0

    def main_menu(self):
        if self.current_stage == 0:
            usr_menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
            if usr_menu == 'play':
                self.current_stage = 1
            elif usr_menu == 'results':
                self.current_stage = 2
            elif usr_menu == 'exit':
                return 'exit'
            else:
                pass
        elif self.current_stage == 1:
            self.play_the_game()
        elif self.current_stage == 2:
            print(f'You won: {self.win_num} times.\n'
                  f'You lost: {self.lose_num} times.')
            self.current_stage = 0

    @staticmethod
    def input_incorrect(usr_input, tries_list):
        if len(usr_input) != 1:
            print('Please, input a single letter.')
            return True
        elif not usr_input.isalpha() or not usr_input == ''.join(re.findall('[a-z]', usr_input)):
            print('Please, enter a lowercase letter from the English alphabet.')
            return True
        elif usr_input in tries_list:
            print("You've already guessed this letter.")
            return True

    def play_the_game(self):
        usr_life = 8
        guess_word = random.choice(self.dic_words)
        hidden_char_str = list('-' * (len(guess_word)))
        usr_letters = []
        while usr_life > 0:
            index_4_search = 0
            list_indexes = []
            print('')
            print(''.join(hidden_char_str))
            usr_letter = input('Input a letter: ')
            if self.input_incorrect(usr_letter, usr_letters):
                continue
            usr_letters.append(usr_letter)
            if guess_word.find(usr_letter) == -1:
                print("That letter doesn't appear in the word.")
                usr_life -= 1
            else:
                while guess_word.find(usr_letter, index_4_search) >= 0:
                    list_indexes.append(guess_word.find(usr_letter, index_4_search))
                    index_4_search = guess_word.find(usr_letter, index_4_search) + 1
                    for i in list_indexes:
                        hidden_char_str[i] = usr_letter
            if ''.join(hidden_char_str) == guess_word:
                print(f'You guessed the word {guess_word}!\n'
                      'You survived!')
                self.win_num += 1
                self.current_stage = 0
                break
        else:
            print('\n'
                  'You lost!')
            self.lose_num += 1
            self.current_stage = 0


usr_1 = Hangman()
x = ''
print('H A N G M A N')
while x != 'exit':
    x = usr_1.main_menu()
