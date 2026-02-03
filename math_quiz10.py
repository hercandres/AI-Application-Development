# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 10:00:51 2026

@author: Personal
"""

import random as r


def pick_operation():
    x = r.randint(1,4)
    if x == 1:
        retorno = "+"
    elif x == 2:
        retorno = "-"
    elif x ==3:
        retorno = "*"
    else:
        retorno = "/"
    return retorno

def pick_numbers():
    y = r.randint(0, 100)
    return y

def init():
    correct = 0
    wrong = 0
    
    print("Welcome to your math questions practice\n" )
    for x in range(0,10):
        operation = pick_operation()
        number1 = pick_numbers()
        number2 = pick_numbers()
        
        if operation == "+":
            print("Your operation is: " + str(number1) + " + " + str(number2) + " =")
            answer = number1 + number2
            user = int(input("Please enter your answer:"))
            if answer == user:
                print("Your answer is correct!!")
                correct += 1
            else:
                print("Your answer is wrong")
                wrong += 1
                
        elif operation == "-":
            print("Your operation is: " + str(number1) + " - " + str(number2) + " =")
            answer = number1 - number2
            user = int(input("Please enter your answer:"))
            if answer == user:
                print("Your answer is correct!!")
                correct += 1
            else:
                print("Your answer is wrong")
                wrong += 1
                
        elif operation == "*":
            print("Your operation is: " + str(number1) + " * " + str(number2) + " =")
            answer = number1 * number2
            user = int(input("Please enter your answer:"))
            if answer == user:
                print("Your answer is correct!!")
                correct +=  1
            else:
                print("Your answer is wrong")
                wrong += 1
        
        else:
            print("Your operation is: " + str(number1) + " / " + str(number2) + " = ")
            answer = float(number1 / number2)
            answer = round(answer,1)
            user = float(input("Please enter your answer (round to 1 decimal place if needed):"))
            if answer == user:
                print("Your answer is correct!!")
                correct +=  1
            else:
                print("Your answer is wrong")
                wrong += 1
            
    print("Correct answers = " + str(correct))
    print("Incorrect answers = " + str(wrong))
    percent = round(   (  (correct*100)/(correct+wrong)  )   ,1)
    print("Accuracy level: " + str(percent) + " %")
        
    return None


init()