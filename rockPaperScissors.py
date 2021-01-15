#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:02:04 2021

@author: McBride
"""

import random
import pyinputplus as pyip

def introText():
    print("----------------------------------------")
    print("Welcome to Rock Paper Scissors!")
    print()
    play=pyip.inputYesNo("Best two out of three. Do you think you can"\
                         " beat me? (yes/no)")
    if play == 'yes':
        game()
    else:
        print("Okay, see you next time!")
def finalScore(user,comp):
    if user > comp:
        print()
        print("You beat me!")
        print("The score was {} to {}.".format(user,comp))
        print()
        print("I want a rematch.")
        play_again=pyip.inputYesNo("Want to play again? (yes/no)")
        if play_again=='yes':
            print("Good choice!")
            game()
        else:
            print("Okay, see you next time!")
    elif comp < user:
        print()
        print("Good game!")
        print("I won this one {} to {}.".format(comp,user))
        print()
        play_again=pyip.inputYesNo("Want to play again? (yes/no)")
        if play_again=='yes':
            print("Challenge accepted!")
            game()
        else:
            print("Okay, see you next time!")
            
def compChoice():
    shoot=['Rock','Paper','Scissors']
    comp_choice=random.choice(shoot)
    return(comp_choice)

def game():
    comp_score=0
    user_score=0
    while comp_score < 2 and user_score < 2:
        print("Make your choice: 'Rock', 'Paper' or 'Scissors'")
        print("Ready?")
        user_choice=pyip.inputChoice(('Rock','Paper','Scissors'),prompt=""\
                                     "Rock, Paper, Scissors. Shoot!")
        comp_choice=compChoice()
        if user_choice==comp_choice:
            print()
            print("You chose {}".format(user_choice))
            print("I chose {}".format(comp_choice))
            print("We tied!")
            print()
            print("Score:")
            print("You've won {}.".format(user_score))
            print("I've won {}.".format(comp_score))
        elif user_choice=='Rock':
            if comp_choice=='Paper':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(comp_choice,user_choice))
                print()
                comp_score=comp_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
            elif comp_choice=='Scissors':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(user_choice,comp_choice))
                print()
                user_score=user_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
        elif user_choice=='Paper':
            if comp_choice=='Scissors':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(comp_choice,user_choice))
                print()
                comp_score=comp_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
            elif comp_choice=='Rock':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(user_choice,comp_choice))
                print()
                user_score=user_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
        elif user_choice=='Scissors':
            if comp_choice=='Rock':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(comp_choice,user_choice))
                print()
                comp_score=comp_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
            elif comp_choice=='Paper':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(user_choice,comp_choice))
                print()
                user_score=user_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
    else:
       finalScore(user_score,comp_score)
       
introText()

       
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                