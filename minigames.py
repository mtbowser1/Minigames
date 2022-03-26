#minigames v1.01
#Sample code project, features some basic minigames and python exercises
#Marshall Bowser, 3/22/22

from random import * #imports the random library which we need for most of our games to work, the asterisk denotes everything in the library
#alternatively, we could import a single function if we desired

name = "Marshall" #keeps things from breaking in the functions before we have an official name

#functions are first, despite coming first in the code these are not actually called until later in the program menu
#its important to note all these run when the program starts despite not generating output until later - if there are errors and unreferenced variables, the program won't compile
#the idea is that this compartmentalizes the program and regulates issues to a smaller area while keeping larger pieces of program functional
#this is especially important for larger programs with multiple team members, but can also be helpful for reviewing legacy code
def trashtalkwin():
    ttwin = ['Relax, it gets easier to accept each time it happens.', 'Hahahah!', 'I love knocking humans down a peg.', 'WOW!', 'Look, computers were going to win eventually, right?'] #an array of strings
    random = randrange(len(ttwin)) #measures the array and returns an integer, then uses this as the limit for a random integer function, the array can be added on to or removed from without breaking the code
    return ttwin[random] #returns a statement when called randomly picked from the array above

def trashtalklose():
    ttlose = ['I am programmed to lose, so what is your excuse?', 'Everybody gets lucky eventually.', 'Hmph!', 'Is this what sadness feels like?', 'You must really be proud of yourself, hmm?']
    random = randrange(len(ttlose))
    return ttlose[random]

def rps(): #minigame is broken into a function, demonstrates OOP coding practices
    playerwin = 0 #defines a variable and starts it at 0, the game will later track the wins in the loop
    playerlose = 0
    while 1:
        print("Let's play rock, paper, scissors "+name+"! I promise I won't cheat!") #basic output command, calls a variable named 'name'
        print("Pick rock, paper, or scissors... or you can quit if you want.")
        while 1:
            rpschoice = str(input())
            if rpschoice == 'rock' or rpschoice == 'scissors' or rpschoice == 'paper' or rpschoice == 'quit': #or operands let us do this in a single line
                break #breaks the while loop, executes the first line after the indentation
            else: #this handles errors in our input
                print("You must choose rock, paper, scissors, or quit.")
        if rpschoice == 'quit': #gives the user a way to go back to menu without ending program
            break
        compchoice = randrange(3) #produces a random integer between 0-2, perfect for our game
        print("Rock, paper, scissors, shoot!")
        if compchoice == 0 and rpschoice == 'rock':
            print("We picked the same thing, "+rpschoice+". A tie, then!")
        elif compchoice == 0 and rpschoice == 'paper':
            print("I picked rock! I lose!")
            playerwin = playerwin+1 #adds a point to the score for the print statement at the end of the function, increases each time
            print(trashtalklose()) #calls a trash talk function above with an array of trash talk statements randomly picked within the function itself
        elif compchoice == 0 and rpschoice == 'scissors':
            print("I picked rock! I win!")
            playerlose = playerlose + 1
            print(trashtalkwin())
        elif compchoice == 1 and rpschoice == 'rock':
            print("I picked paper! I win!")
            playerlose = playerlose + 1
            print(trashtalkwin())
        elif compchoice == 1 and rpschoice == 'paper':
            print("We picked the same thing, "+rpschoice+". A tie, then!")
        elif compchoice == 1 and rpschoice == 'scissors':
            print("I picked paper! I lose!")
            playerwin = playerwin + 1
            print(trashtalklose())
        elif compchoice == 2 and rpschoice == 'rock':
            print("I picked scissors! I lose!")
            playerwin = playerwin + 1
            print(trashtalklose())
        elif compchoice == 2 and rpschoice == 'paper':
            print("I picked scissors! I win!")
            playerlose = playerlose + 1
            print(trashtalkwin())
        elif compchoice == 2 and rpschoice == 'scissors':
            print("We picked the same thing, "+rpschoice+". A tie, then!")
        print("You've won", playerwin, "games "+name+" and I've won", playerlose, "games.") #you need to use this print format for integers mixed with string statements to prevent errors

def riddleFunction():
    while 1:
        #a challenge is making similar concepts distinct - i can have a function called riddles, for example, but a dictionary called riddles might make problems down the road
        riddleDict = {'What 4-letter word can be written forward, backward or upside down, and can still be read from left to right? (riddles.com)': 'Noon',
                      'What is full all day and empty at night? (riddles.com)': 'Shoes',
                      'What has to be broken before you can use it? (fatherly.com)': 'Egg',
                      'What has many ears but cannot hear?': 'Corn',
                      'The more you take, the more you leave behind (fatherly.com)': 'Footsteps',
                      'When things go wrong, what can you always count on? (fatherly.com)': 'Fingers',
                      'What goes up but never goes back down? (fatherly.com)': 'Age',
                      'What can you catch but not throw? (fatherly.com)': 'Cold',
                      'What belongs to one person, but everyone else it more? (fatherly.com)': 'Name',
                      'Where can you find cities, towns, shops, and streets but no people? (fatherly.com)': "Map"
        }
        random = randrange(len(riddleDict.keys())) #chooses a random integer based on the size of our dictionary - dictionary can be modified and code remains functional
        riddleValues = list(riddleDict.values()) #creates a list of values
        riddleKeys = list(riddleDict.keys()) #creates a list of keys
        print(riddleKeys[random]) #using the same random integer above we print a key, or question
        answer = input(str()) #gets input
        answer = answer.lower() #cleans up the input a bit, accepts capitilzation variations (No, NO)
        if answer == riddleValues[random].lower(): #compares value, or answer, to the input which is also cleaned for capitilization
            print("You got it right! Well done.")
        else:
            print("I'm sorry, that wasn't right. The answer is ", riddleValues[random], ".", sep='') #the seperator feature with no input eliminates the extra space around the period
        print("Would you like to play again or quit?")
        answer2 = input(str())
        answer2 = answer2.lower()
        if answer2 == 'no':
            break
        elif answer2 == 'quit':
            break
        else:
            print('OK!')


#the following lines are the first text in the program the user sees
print("What is your name?")
name = str(input()) #prompts for input, typed input becomes a string called name
print("Hi "+name+"!")

#this loop serves as a menu for our program, the user won't be prompted for a name multiple times since it's not in the loop
while 1: #loops a menu, else statement handles errors on bad input without crashing program
    print("~~~~~ Minigame Menu ~~~~~")
    print("Please choose a function.")
    print("1. Rock, Paper, Scissors.")
    print("2. Riddle Me This.")
    print("0. Quit.")
    menuchoice = str(input()) #string statement prevents a program crash from non-integer input
    if menuchoice == '1':
        rps()
    elif menuchoice == '0':
        exit()
    elif menuchoice == '2':
        riddleFunction()
    else:
        print("Pick an integer between 0 and 9.")