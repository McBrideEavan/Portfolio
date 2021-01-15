#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:35:03 2021

@author: McBride
"""

import random
import pyinputplus as pyip

#Intro text to introduce user to program
def introText():
    print("--------------------------------------------------")
    print("Welcome adventurer!")
    print()
    print("My name is Hubbard.")
    print()
    print("I am the wizard that rolls the dice of fate.")
    play=pyip.inputYesNo("Do you seek my wisdom? (yes/no)")
    #if they agree to play
    if play == 'yes':
        dndRolls()
    #if thay want to exit
    else:
         print()
         print("Good luck, adventurer!")
         print("May the fates decide in your favor.")
#function that contains dice rolling   
def dndRolls():
    print("How many sides should the fates consider?")
    #get number of sides the dice needs
    sides=pyip.inputInt("Give me ___-sided dice.",min=1, max=20) 
    print("And how many fortunes do you dare to roll?")
    #get number of dice to roll
    dice=pyip.inputInt("Roll ___ dice.",min=1)
    print()
    print("The fates have spoken.")
    print()
    #define loop trigger
    rolls=0
    #roll for specified number of dice
    while rolls < dice:
        roll=random.randint(1,sides)
        #redefine loop trigger
        rolls=rolls+1
        #print result of dice roll
        print("Fortune {}:".format(rolls),roll)
        print()
    else:
        #When all dice are rolled ask if they want to roll again
        roll_again=pyip.inputYesNo("Do you seek further wisdom?"\
                                   "(yes/no)")
        #if yes send back to top of function
        if roll_again == 'yes':
            dndRolls()
        #if no, exit text
        else:
            print()
            print("Good luck, adventurer!")
            print("May the fates decide in your favor.")

#call function
introText()
    

