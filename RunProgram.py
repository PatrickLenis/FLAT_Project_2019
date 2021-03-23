#Main menu for the code

import AbstractSyntax

#Data

#Introduction

print("\nConstruct a DFA equivalent to an Regular Expression\nBy Patrick Lenis and Paul Cvasa")

#Input

print("\nA regular Expression can contain letters from the english alphabet as well as the simbols |, *.\nThe input requieres parantheses ( ex. : (x|((XY)*)) )\n")
Input_Expression = input("Input a Regular Expression here : ")

#Checking Input


Checked_Expression_List = []

for character in Input_Expression:
    if character != ' ':
        Checked_Expression_List.append(character)

Checked_Expression = ''.join(Checked_Expression_List)


#Abstract syntax

Abstract_Regular_Expression = AbstractSyntax.Make_Tree(Checked_Expression)
print(Abstract_Regular_Expression)


#Regular Expression to NFA

#NFA to DFA

#Final output
