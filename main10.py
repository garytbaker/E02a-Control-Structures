#!/usr/bin/env python3 #this is a comment
import sys, random #this imports random and sys
                    #this is a bllank line
assert sys.version_info >= (3,7), "This script requires at least Python 3.7" #this makes sure python is at least python 3.7 or newer
                    #this is a bllank line
                    #this is a bllank line
print('Greetings!') #this prints greetings to the terminal
colors = ['red','orange','yellow','green','blue','violet','purple'] #this makes a list containing 7 strings
play_again = ''#this is a empty string
best_count = sys.maxsize            # the biggest number #this sets the best_count variable to the biggest number
                    #this is a bllank line
while (play_again != 'n' and play_again != 'no'):   #this loops while play_again isn't the string 'n' or the string 'no'
    match_color = random.choice(colors) #this sets match_color to a random element in the list colors.
    count = 0               #this sets count to 0
    color = ''                 #this assigns the empty string to the variable color.
    while (color != match_color):       #while the string in color does not match the string in match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line  #gets input from the user asking what the color is.
        color = color.lower().strip() #sets color to the lowercase version without leading or trailing spaces  
        count += 1  #increments count by 1
        if (color == match_color):  #if the color and match color are the same
            print('Correct!')       #it pprints correct
        else:                       #otherwise
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))#it telss the user that they are wrong and asks how many times they guessed
                                    #this is a bllank line    
    print('\nYou guessed it in {} tries!'.format(count))    #after the loop it tells them how many times they guessed to get it correct
                                    #this is a bllank line
    if (count < best_count):        #if the count less than the best_count variable
        print('This was your best guess so far!')   #prints that they guessed in less tries than previously
        best_count = count                          #sets best count to count
                                    #this is a bllank line
    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()  #asks if they want to play again and then sets the answer to the play_again ariable in all owercase with no preceding or trailing spaces.
                                    #this is a bllank line
print('Thanks for playing!')        #thanks the user for playing before exiting