
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
	It will print Greetings to ther terminal followed by a line asking for a favorite color and then wait for input.
  
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
    It printed Greetings to ther terminal followed by a line asking for a favorite color and then waited for input.
  
  - What do you think the program did with what you typed in answer to the question?
    nothing.
- Open main02.py. Before running it, describe how this is different than main01.py.
  It stores the input into a variable and then prints it out instead of just asking for input.
  
  - What do you think the color = input() will do?
    It will store the input into the variable.
  
  - Run the program in the terminal and answer the question. Did the program do what you expected?
    Yes, it did what I expected it to do.
- Open main03.py. Before running it, describe how this is different than main02.py.
  It checks to see if they entered the string 'Red' and if they did it prints Correct! and if they entered anything else it asks them to try again.

  - What is happening on lines 9–12?
    There is an if else statement.
  
  - Why are lines 10 and 12 indented?
    because Python is a whitespace language and that is how it tells it is a block of code.

  - Run the program and answer the question. What happens if you don’t capitalize Red?
    it says false because it checks to see if it matches the string exactly.
  
  - What does this tell you about "color"?
    It is a string and things like capitalization matter.

- Open main04.py. Before running it, describe how this is different than main03.py.
  It checks to for bot the string 'Red' and the string 'red'.
  
  - What problem is this trying to solve?
    it is trying to solve the problem of capitalization.

  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
    It still fails.

- Open main05.py. What do you expect line 9 to do?
  It converts color to a lowercase version of itself and then checks to see it matches the string 'red'.

  - What problem is it trying to solve?
    It is still trying to solve the capitilization problem.

  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
    It fails because space is still a whitespace caracter so the string ' red' != 'red'

 - Open main06.py. How is line 9 different than in main05.py?
  It calss the .strip() function wich removes any leading or trailing spaces.

  - What would you guess .strip() is doing?
    It is removing the trailing or leading spaces.

  - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
    It removed the trailing and leading spaces but 'r e d' wouldbreak the logic.

- Open main07.py. Before running this program, how do you expect this to be different than main06.py?
  it checks using elif if the color is equal to the string 'pink' as well and prints Close! if it is pink.

  - What is happening on line 12?
    That is an elif statement. it stands for else if. So if that condition is true and all previous if/elif statements were false, that one would be run.

  - Run the program and answer the question.
    It first checks to see if the color was red, and since it wasn't, it checked to see if the color was pink, then if it wasn't it ran the else statement.


- Open main08.py. What is the purpose of line 9?
  It is a loop that will run while the color does not equal the string 'red'

  - Why are lines 10–17 indented?
    they are indented because python is a whitespace language and they are the block of code for the while loop.


  - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
    The loop would go infinte after asking for the color if it was not red. 

  - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
    The loop went infinte after asking for the color since it was not red.

- Open main09.py. What is happening on line 13?
  It assigns the value of count to be itself + 1. This will happen every cycle in the loop.

  - What is the purpose of “count”?
    It keeps track of the number of tries at guessing the favorite color.

  - What is happening on line 22?
    there is not a line 22, so i assume that you mean line 21. It is just printing out the number of attempts 
    at trying to guess the color using the .format function of print.

  - Run the program.
    Ok.


- *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a 
pound sign [#]).
 
 
- *Extra credit:* open main11.py. What is happening on lines 6-11?
  It is creating a function called choose color which takes in a string and then generates a random string from the list. While the sting it took in and the string it generated are the same, it generates a new string until the two are different, and then returns that value. This essentially chooses a new color that is different than the last color.
  
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
