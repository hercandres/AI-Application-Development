# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:10:12 2026

@author: Personal
"""

def get_question():
    user = input("Please enter your math question, dont include empty spaces between number or operators. \nMake sure to separte the operation from any other characters\n")
    return user

def find_digits()->list:
    w = get_question()
    split_question = w.split()
    
    for word in range(0,len(split_question)):
        if split_question[word][0].isdigit():
            for character in range(0,len(split_question[word])):
                if split_question[word][character] == "+":
                    numbers = split_question[word].split("+")
                    operator = "+"
                    break
                
                elif split_question[word][character] == "-":
                    numbers = split_question[word].split("-")
                    operator = "-"
                    break
                
                elif split_question[word][character] == "/":
                    numbers = split_question[word].split("/")
                    operator = "/"
                    break
                
                elif split_question[word][character] == "*":
                    numbers = split_question[word].split("*")
                    operator = "*"
                    break
                
    lista = [numbers[0],numbers[1],operator]
    
    return lista

def answer_question(lista):
    number1 = float(lista[0])
    number2 = float(lista[1])
    
    if lista[2] == "+":
        respuesta = number1 + number2 
    elif lista[2] == "-":
        respuesta = number1 - number2
    elif lista[2] == "/":
        respuesta = number1 / number2
    else:
        respuesta = number1 * number2
        
    message = str(number1) + " " + lista[2] + " " + str(number2) + " = " + str(respuesta)
    
    return message

def init():
    x = find_digits()
    print(answer_question(x))


init()
    

    
    