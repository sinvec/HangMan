#!/usr/bin/env python
from __future__ import print_function
from builtins import input
from termcolor import colored
import readchar
from random import randint
import sys
import os
import time
from .data import *
import threading,time
from threading import Lock

data_dir = os.path.join(os.path.dirname(__file__),'data')

terminal_sprites = read_from_disk(some_path)

class Game:

    win = 0
    lose = 0

    success_status = 0
    fraim_number = 0
    animal = 'dog'
    blanks = '_'
    done_letters = ['ij']
    

    def __init__(self, words):
        print(words)
        self.animal = words[randint(0,len(words)-1)].upper()
        self.blanks = len(self.animal) * '_'
        for letter_index, letter in enumerate(self.animal):
            if not letter.isalpha():
                self.blanks = self.blanks[:letter_index] + letter + self.blanks[letter_index+1:]
        os.system("clear")
    
    def update_score(self):
        if self.success_status == 1:
            Game.win += 1 
        else:
            Game.lose += 1

    def reset_done_letters():
        self.done_letters = []
        return self.done_letters

    def print_status(self): 
        print("Score is", colored("win = " + str(Game.win), 'green'), "\\", colored("lose = "+ str(Game.lose), 'red') )
    
    def start(self):
        while True:
            os.system("clear")
            print (colored(terminal_sprites['active'][self.fraim_number],'magenta'))
            for blank_index in range(len(self.blanks)):
                print(self.blanks[blank_index], end= ' ')
            print()
            print(colored("DONE LETTERS:",'blue'), end='')
            print(*self.done_letters, sep=',')
            while True:
                entered_letter = input("Your choice of letter?")
                if len(kentered_letter) != 1:
                    print('Enter only one letter please')
                    continue
                elif not entered_letter.isalpha():
                    print('Enter only alphabets')
                    continue
                elif entered_letter.upper() in self.done_letters:
                    print ('The letter entered is already done')
                    continue
                else:       
                    entered_letter = entered_letter.upper()
                    self.done_letters.append(entered_letter)
                    break
                    
            if self.animal.find(k) !=- 1:
                word_index = 0
                while word_index < len(self.animal):
                    if self.animal[i] == k:
                        self.blanks = self.blanks[:word_index] + k + self.blanks[word_index+1:]
                    word_index += 1   
            else:
                self.fraim_number = self.fraim_number + 1
            
            if self.blanks.find('_') == -1: # No blanks found
                print('entered')
                self.fraim_numberuccess_status = 1
                break
                    
            if self.fraim_number == len(terminal_sprites['active']): # Hangman Complete
                self.fraim_numberuccess_status = 0
                break

class Terminal:

    key = None

    def get_key_press():
        while Terminal.key != 'q':
            Terminal.key = readchar.readchar()
            if Terminal.key == '\x03':
                raise KeyboardInterrupt

    def start_screen():
        pressed_keys_number = 0
        try:
            while Terminal.key != 'q':
                os.system("clear") 
                print(colored(terminal_sprites['active'][pressed_keys_number%7],'green'))
                print (colored('##### WELCOME TO THE GAME OF HANGMAN #####','yellow'))
                print (colored('####### Save the man from hanging ########','cyan'))
                if pressed_keys_number % 2 == 0:
                    print (colored('       [press <Ctrl + c> to start]','red'))
                time.sleep(0.5)
                pressed_keys_number += 1
        except:
            pass

    def select_type():
        os.system("clear")
        print(colored("Rules: Guess the word letter by letter to save the man from hanging",'blue'))
        print(colored("\n\n\t\tSelect word list\n\t\t1. Animals\n\t\t2. Pokemons\n\t\t3. Fruits\n\t\t4. Countries\n\t\t5. Bollywood Movies","magenta"))
        file_name = None
        list_type = None
        while True:
            entered_letter = readchar.readchar() 
            if entered_letter == '1': 
                file_name = 'animals.txt'
                list_type = 'animals'
                break
            elif entered_letter == '2':
                file_name = 'pokemons.txt'
                list_type = 'pokemons'
                break
            elif entered_letter == '3':
                file_name = 'fruits.txt'
                list_type = 'fruits'
                break
            elif entered_letter == '4':
                file_name = 'countries.txt'
                list_type = 'fruits'
                break
            elif entered_letter == '5':
                file_name = 'bollywood movies.txt'
                list_type = 'bollywood movies'
                break
            elif entered_letter == '\x03':
                raise KeyboardInterrupt

        return list_type, word_list[list_type]

    # Function for animation after win or lose
    # Takes a Game class object as input
    def hanging_man_anim(game):  
        pressed_keys_number = 0    
        if game.success_status == 0:
            while pressed_keys_number <= 4:
                os.system("clear")
                if pressed_keys_number % 2 == 0:
                    print(colored(terminal_sprites['hanged'],'red'))
                else:
                    print(colored(terminal_sprites['active'][-1],'red'))
                print(colored(":( !Man Hanged! :(\nCorrect word: ",'red')+colored(game.animal,'green'))
                game.print_status()
                time.sleep(0.5)
                pressed_keys_number += 1
        else:
            while pressed_keys_number <= 4:
                os.system("clear")
                if pressed_keys_number % 2 == 0:
                    print(colored(terminal_sprites['free'][0],'green'))
                else:
                    print(terminal_sprites['free'][1])
                print(colored(":) !Man Saved! :)",'green'))
                game.print_status()
                time.sleep(0.5)
                pressed_keys_number += 1

def main():
    Terminal.start_screen()
    _, words = Terminal.select_type()
    print(words)

    while True:
        
        game = Game(words)
        game.reset_done_letters()
        game.start()
        game.update_score()

        Terminal.hanging_man_anim(game)
        
        exit_question = input("another game?(y/n)")
        break_flag = 0
        while True:
            if (exit_question =='y'):
                break
            elif (exit_question == 'n'):
                break_flag = 1
                break   
            else:
                exit_question = input("please type (y/n)")

        if break_flag != 0:
           break
