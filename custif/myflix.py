#!/usr/bin/env python3

def askUser():
    loop = True; 
    while loop == True:

        listA = ['English', 'Microsoft','Pain', 'Web', 'Money', 'Unemployment']

        reply1 = " "
        output = ""
        again = True;
        print("~A TEST TO DETERMINE WHAT PROGRAMMING LANAGUE IS BEST SUITED FOR YOU~\n")


        while reply1 not in listA:
            reply1 = input("Choose a word you can relate to the most:\n English, Unemployment, Microsoft, Pain, Web, Money: ").title()


        if reply1 == 'English':
            message = 'Python'

        elif reply1 == 'Microsoft':
            message = 'C#'

        elif reply1 == 'Pain' :
            message= 'C++'

        elif reply1 == 'Web':
            message = 'JavaScript'

        elif reply1 == 'Money':
            message = 'Scala'

        elif reply1 == 'Unemployment':
            message = 'Visual Basic'

        print(f"\nYou should learn {message}!\n")

        goAgain= input("Would you like to go again?Type \"No\" to exit  ").title()
        if goAgain == 'No':
            loop = False;

askUser()


