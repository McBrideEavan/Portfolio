#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:35:03 2021

@author: McBride
"""

import random
import pyinputplus as pyip


def introText():
    print("--------------------------------------------------")
    print("Welcome adventurer!")
    print()
    print("My name is Hubbard.")
    print()
    print("I am the wizard that rolls the dice of fate.")
    play=pyip.inputYesNo("Do you seek my wisdom? (yes/no)")
    if play == 'yes':
        dndRolls()
    else:
         print()
         print("Good luck, adventurer!")
         print("May the fates decide in your favor.")
    
def dndRolls():
    print("How many sides should the fates consider?")
    sides=pyip.inputInt("Give me ___-sided dice.",min=1, max=20) 
    print("And how many fortunes do you dare to roll?")
    dice=pyip.inputInt("Roll ___ dice.",min=1)
    print()
    print("The fates have spoken.".format(dice, sides))
    print()
    rolls=0
    while rolls < dice:
        roll=random.randint(1,sides)
        rolls=rolls+1
        print("Fortune {}:".format(rolls),roll)
        print()
    else:
        roll_again=pyip.inputYesNo("Do you seek further wisdom?"\
                                   "(yes/no)")
        if roll_again == 'yes':
            dndRolls()
        else:
            print()
            print("Good luck, adventurer!")
            print("May the fates decide in your favor.")

introText()
    

