# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:14:48 2026

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
    answerlist = []
    quiz = open("quiz.txt",'w')
    quiz.write("Quiz\n")
    
    
    for x in range(0,10):
        operation = pick_operation()
        number1 = pick_numbers()
        number2 = pick_numbers()
        
        if operation == "+":
            answer = number1 + number2
            answerlist.append(answer)
            
                
        elif operation == "-":
            answer = number1 - number2
            answerlist.append(answer)
            
        elif operation == "*":
            answer = number1 * number2
            answerlist.append(answer)
            
        
        else:
            answer = float(number1 / number2)
            answer = round(answer,1)
            answerlist.append(answer)
                
        quiz.write("Question #" + str(x + 1) + "\n")
        quiz.write(str(number1) + " " + str(operation) + " " + str(number2) + ":\n")
        
        
    quiz.write("\n")
    quiz.write("Correct Answers: \n")
    
    for y in range (0, len(answerlist)):
        quiz.write("Question " + str(y+1) + ": " + str(answerlist[y]) + "\n")
    
    return None


init()