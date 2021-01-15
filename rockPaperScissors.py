#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:02:04 2021

@author: McBride
"""

import random
import pyinputplus as pyip


#introduce user to the program
def introText():
    print("----------------------------------------")
    print("Welcome to Rock Paper Scissors!")
    print()
    #ask if they want to play
    play=pyip.inputYesNo("Best two out of three. Do you think you can"\
                         " beat me? (yes/no)")
    #start game
    if play == 'yes':
        game()
    #or exit program
    else:
        print()
        print("Okay, see you next time!")
        
#display final score and play again/exit text       
def finalScore(user,comp):
    #if the user won
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
            print()
            print("Okay, see you next time!")
    #if the user lost
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
            print()
            print("Okay, see you next time!")
   
#generate computer choice for game
def compChoice():
    shoot=['Rock','Paper','Scissors']
    comp_choice=random.choice(shoot)
    return(comp_choice)

#game functionality
def game():
    #define loop triggers
    comp_score=0
    user_score=0
    #if neither has won then keep playing
    while comp_score < 2 and user_score < 2:
        print("Make your choice: 'Rock', 'Paper' or 'Scissors'")
        print("Ready?")
        #get user choice
        user_choice=pyip.inputChoice(('Rock','Paper','Scissors'),prompt=""\
                                     "Rock, Paper, Scissors. Shoot!")
        #generate computer choice
        comp_choice=compChoice()
        #if they are the same
        if user_choice==comp_choice:
            print()
            print("You chose {}".format(user_choice))
            print("I chose {}".format(comp_choice))
            print("We tied!")
            print()
            print("Score:")
            print("You've won {}.".format(user_score))
            print("I've won {}.".format(comp_score))
        #if the user chose rock
        elif user_choice=='Rock':
            #compare to computer choice
            if comp_choice=='Paper':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(comp_choice,user_choice))
                print()
                #redefine loop trigger
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
                #redefine loop trigger
                user_score=user_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
        #if the user choce paper
        elif user_choice=='Paper':
            #compare to computer choice
            if comp_choice=='Scissors':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(comp_choice,user_choice))
                print()
                #redefine loop trigger
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
                #redefine loop trigger
                user_score=user_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
        #if the user chose scissors
        elif user_choice=='Scissors':
            #compare to computer choice
            if comp_choice=='Rock':
                print()
                print("You chose {}".format(user_choice))
                print("I chose {}".format(comp_choice))
                print("{} beats {}!".format(comp_choice,user_choice))
                print()
                #redefine loop trigger
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
                #redefine loop trigger
                user_score=user_score+1
                print("Score:")
                print("You've won {}.".format(user_score))
                print("I've won {}.".format(comp_score))
    #when someone has won(i.e. gotten 2 wins)
    else:
       finalScore(user_score,comp_score)
       
introText()

       
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                