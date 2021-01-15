#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:54:04 2021

@author: McBride
"""

#The program generates a random number 1 to 100 
#the user must guess the number after a hint from the computer. 
#Every time a user’s guess is wrong they are prompted with more hints
#at the cost of reducing the score. 
 

#allows random generation of numbers
import random
#moderates acceptable user input and reprompts where needed
import pyinputplus as pyip

#set list variable to track best score
best_score=[]

#define best score function to calc and list best score
def bestScore():
    #if there is no best score
    if len(best_score) ==0:
        print("We don't have a high score....yet.")
    #otherwise...
    else:
        print("The current high score is {} guesses!".format(min(best_score)))

#define function for the game
def guessGame():
    #start attempt count for high score
    attempts=0
    #generate random number
    answer=random.randint(1,100)
    #intro text
    print("-----------------------------------------")
    print("Welcome to the guessing game!")
    print()
    #print current best score
    bestScore()
    print()
    print("I am thinking of a number between 1 and 100.")
    #define loop trigger
    play_game=pyip.inputYesNo("Can you guess the number? (y/n)",yesVal='y',noVal='n')
    if play_game == 'y':
        print()
        print("Challenge Accepted!")
    #start loop *loop will continue to run until the user wins 
    #and the loop trigger is redefined
    while play_game == 'y':
        #request user guess
        guess=pyip.inputInt("Choose a number between 1 and 100:",min=1,max=100)
        #when correct
        if answer==guess:
            #redefine attempts score
            attempts=attempts+1
            #add score to best_score list
            best_score.append(attempts)
            #congrats text
            print()
            print("You guessed it!")
            print()
            print("It took you {} guesses.".format(attempts))
            #print best score
            bestScore()
            print()
            print("------------------------------------------------")
            #redefine loop trigger
            play_game=pyip.inputYesNo("Would you like to play again? (y/n)",yesVal='y',noVal='n')
            #redefine attempts so the next game has a new count
            attempts=0
            #if they want to play again
            if play_game=='y':
                #generate new random number
                answer=random.randint(1,100)
                #print transition text then loop will start again 
                print()
                print("Good choice!")
                print("I'm thinking of a new number...")
        #or if too high
        elif answer < guess:
            print("That number is too high.")
            print()
            #redefine attempts score
            attempts=attempts+1
        #or if too low
        elif answer > guess:
            print("That number is too low.")
            print()
            #redefine attempts score
            attempts=attempts+1
    else:
        #generate new random number
        end_number=random.randint(1,100)
        #exit text
        print("-------------------------------------------------")
        print("No problem.")
        print("My next number was {}, would you have guessed it?".format(end_number))
        print("See you next time!")
        
#CALL FUNCTION    
guessGame()