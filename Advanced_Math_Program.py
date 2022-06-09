from random import randint
import os


def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")

class settings:
    set_objective = 3
    set_lives = 3

class setValue: 
    additionNum_1 = 0
    additionNum_2 = 0
    subtractionNum_1 = 0
    subtractionNum_2 = 0
    subtractionNum_3 = 0
    subtractionNum_4 = 0
    multiplicationNum_1 = 0
    multiplicationNum_2 = 0
    multiplicationNum_3 = 0
    multiplicationNum_4 = 0
    divisionNum_1 = 0
    divisionNum_2 = 0
    divisionNum_3 = 0
    divisionNum_4 = 0


def display_separator(icon):
    print(icon * 31)

def operator_display():
    operator_list = ['1. Addition (+)', '2. Subtraction (-)', '3. Multiplication (*)', '4. Devision (/)']
    for operator in operator_list:
        print(operator)
    display_separator(' ')


def difficulty_display():
    difficulty_list = ['1. Easy :)', '2. Medium :|', '3. Hard >:(', '4. EXTREME \>_</']
    print('Select a difficulty: ')
    display_separator(' ')
    for difficulty in difficulty_list:
        print(difficulty)
    display_separator(' ')
    

def gamemode_display():
    gamemode_list = ['1. 10 Questions', '2. 25 Questions', '3. 50 Questions', '4. Rouge Mode (endless questions, one life)', '5. Custom Rules [EXPERIMENTAL]']
    for gamemode in gamemode_list:
        print(gamemode)
    display_separator(' ')


def help_display():
    help_message = '''

Menu Selecting: 
    To select a option in a menu, enter the number in front of the option you choose.

    Example -> 1. 10 Questions

Standard Gamemodes (10, 20, 50 questions):
    For each game you start in this catagory, you start off with 3 lives.  In order to win, answer enough questions to
    meet the objective (which ever gamemode you choose). If you get a question wrong, you lose 1 life. If you lose all
    3 lifes, than its game over.

Rouge Mode:
    When selcting this gamemode, instead of starting with 3 lives, you start with 1.  Different from the standard gamemode's
    where you have a clear objective, in Rogue Mode, you can go on for as long as you want. However if you answer a question 
    wrong, you lose your 1 life and the game is over. Answer wisley.

Custom Rules [EXPERIMENTAL]:
    Feel like mixing it up? Make up your own gamemode with Custom Rules. Add whatever value you want for the objective, lives, 
    math operator, as well as minimum and maximum values for rolling random numbers. WARNING: When setting minimum and maximum
    values, be sure not to set the minimum value higher than maximum, or the maximum lower than minimum. Doing so WILL cause
    the script to crash. 
'''
    print(help_message)


def retry_display(pass_code):
    display_separator(" ")
    while True:

        print('Continue? "yes" to retry. "no" to return back to main menu')
        playAgain = input('Enter your choice: ')

        if playAgain == 'yes' and pass_code == 1:
            select_addition()
        elif playAgain == 'yes' and pass_code == 2:
            select_subtraction()
        elif playAgain == 'yes' and pass_code == 3:
            select_multiplication()
        elif playAgain == 'yes' and pass_code == 4:
            select_devision()
        elif playAgain == 'yes' and pass_code == 5:
            custom_gamemode()
        elif playAgain == 'no':
            menu()
        else:
            print('Invalid input')


def custom_gamemode():
    userScore = 0

    while True:
        try:
            objectiveInput = int(input('Set your objective: '))
            livesInput = int(input("Set how many lives you want: "))
            display_separator(' ')
            operator_display()
            operatorInput = input('Select a math operator: ')
            inputNumber_1 = int(input('Enter a minimum value: '))
            inputNumber_2 = int(input('Enter a maximum value: '))
        except ValueError:
            print('Invalid input')
        else:
            break

    storedValue_1 = inputNumber_1
    storedValue_2 = inputNumber_2
    lives = livesInput
    objective = objectiveInput

    while userScore < objective:
        randomNumber_1 = randint(storedValue_1, storedValue_2)
        randomNumber_2 = randint(storedValue_1, storedValue_2)
        
        if operatorInput == "1":
            operatorInput = "+"
            answer = randomNumber_1 + randomNumber_2
        elif operatorInput == "2":
            operatorInput = "-"
            answer = randomNumber_1 - randomNumber_2
        elif operatorInput == "3":
            operatorInput = "*"
            answer = randomNumber_1 * randomNumber_2
        elif operatorInput == "4":
            operatorInput = "/"
            answer = randomNumber_1 // randomNumber_2        

        print(randomNumber_1, operatorInput, randomNumber_2)

        while True:
            try:
                userGuess = int(input(''))
            except ValueError:
                print('Invalid input')
            else:
                break

        if userGuess == answer:
            display_separator(" ")
            print('CORRECT!')
            userScore += 1
            randomNumber_1 = None
            randomNumber_2 = None
            print('Score:', userScore)
        else:
            display_separator(" ")
            print('INCORRECT!')
            print('Answer:', answer)
            lives -= 1
            print(lives, 'lives left')

            if lives <= 0:
                break
                
    if userScore == objective:
        print('Objective complete. Excellent work!')
    elif lives == 0:
        print('GAME OVER')
        print('Final score:', userScore)
    retry_display(5)


def select_addition():
    userScore = 0
    objective = settings.set_objective
    lives = settings.set_lives
        
    difficulty_display()
    difficultyInput = int(input('Enter a difficulty: '))

    difficulty = difficultyInput
    
    clear()
    while userScore < objective:
        if difficulty == 1:  
            setValue.additionNum_1 = 1
            setValue.additionNum_2 = 30
            easyNum_1 = setValue.additionNum_1
            easyNum_2 = setValue.additionNum_2
            randomNumber_1 = randint(easyNum_1, easyNum_2)
            randomNumber_2 = randint(easyNum_1, easyNum_2)
        elif difficulty == 2:
            setValue.additionNum_1 = 10
            setValue.additionNum_2 = 70
            mediumNum_1 = setValue.additionNum_1
            mediumNum_2 = setValue.additionNum_2
            randomNumber_1 = randint(mediumNum_1, mediumNum_2)
            randomNumber_2 = randint(mediumNum_1, mediumNum_2)
        elif difficulty == 3:
            setValue.additionNum_1 = 30
            setValue.additionNum_2 = 120
            hardNum_1 = setValue.additionNum_1 
            hardNum_2 = setValue.additionNum_2             
            randomNumber_1 = randint(hardNum_1, hardNum_2)
            randomNumber_2 = randint(hardNum_1, hardNum_2)
        elif difficulty == 4:
            setValue.additionNum_1 = 100
            setValue.additionNum_2 = 600
            EXTREMENum_1 = setValue.additionNum_1
            EXTREMENum_2 = setValue.additionNum_2
            randomNumber_1 = randint(EXTREMENum_1, EXTREMENum_2)
            randomNumber_2 = randint(EXTREMENum_1, EXTREMENum_2)

        
        answer = randomNumber_1 + randomNumber_2
          
        print(randomNumber_1, "+", randomNumber_2)
        
        
        while True:
            try:
                userGuess = int(input(''))
            except ValueError: 
                print('Invalid input')
            else:
                break
        

        if userGuess == answer:
      
            display_separator(" ")
            print('CORRECT!')
            userScore += 1
            randomNumber_1 = None
            randomNumber_2 = None
            print('Score:', userScore)
            display_separator(" ")

        elif userGuess != answer:
            display_separator(" ")
            print('INCORRECT!')
            print('Answer:', answer)
            lives -= 1
            print(lives, 'lives left')
            display_separator(' ')

            if lives == 0:
                break


    if userScore == objective:
        display_separator(" ")
        print('Objective complete. Excellent work!')
    elif lives == 0:
        print('GAME OVER')
        print('Final score:', userScore)
    retry_display(1)


def select_subtraction():
    userScore = 0
    objective = settings.set_objective
    lives = settings.set_lives

    difficulty_display()

    while True:
        try:
            difficultyInput = int(input('Enter a difficulty: '))
        except ValueError:
                print('Invalid input')
        else:
            break

    difficulty = difficultyInput

    clear()
    while userScore < objective:
        if difficulty == 1:
            setValue.subtractionNum_1 = 15
            setValue.subtractionNum_2 = 30
            setValue.subtractionNum_3 = 1
            setValue.subtractionNum_4 = 15
            easyNum_1 = setValue.subtractionNum_1
            easyNum_2 = setValue.subtractionNum_2
            easyNum_3 = setValue.subtractionNum_3
            easyNum_4 = setValue.subtractionNum_4
            randomNumber_1 = randint(easyNum_1, easyNum_2)
            randomNumber_2 = randint(easyNum_3, easyNum_4)
        elif difficulty == 2:
            setValue.subtractionNum_1 = 40
            setValue.subtractionNum_2 = 80
            setValue.subtractionNum_3 = 10
            setValue.subtractionNum_4 = 40
            mediumNum_1 = setValue.subtractionNum_1
            mediumNum_2 = setValue.subtractionNum_2
            mediumNum_3 = setValue.subtractionNum_3
            mediumNum_4 = setValue.subtractionNum_4
            randomNumber_1 = randint(mediumNum_1, mediumNum_2)
            randomNumber_2 = randint(mediumNum_3, mediumNum_4)
        elif difficulty == 3:
            setValue.subtractionNum_1 = 60
            setValue.subtractionNum_2 = 120
            setValue.subtractionNum_3 = 15
            setValue.subtractionNum_4 = 60
            hardNum_1 = setValue.subtractionNum_1
            hardNum_2 = setValue.subtractionNum_2
            hardNum_3 = setValue.subtractionNum_3
            hardNum_4 = setValue.subtractionNum_4
            randomNumber_1 = randint(hardNum_1, hardNum_2)
            randomNumber_2 = randint(hardNum_3, hardNum_4)
        elif difficulty == 4:
            setValue.subtractionNum_1 = 240
            setValue.subtractionNum_2 = 960
            setValue.subtractionNum_3 = 50
            setValue.subtractionNum_4 = 240
            EXTREMENum_1 = setValue.subtractionNum_1
            EXTREMENum_2 = setValue.subtractionNum_2
            EXTREMENum_3 = setValue.subtractionNum_3
            EXTREMENum_4 = setValue.subtractionNum_4
            randomNumber_1 = randint(EXTREMENum_1, EXTREMENum_2)
            randomNumber_2 = randint(EXTREMENum_3, EXTREMENum_4)

        answer = randomNumber_1 - randomNumber_2        
        
        print(randomNumber_1, "-", randomNumber_2)
        
        while True:
            try:
                userGuess = int(input(''))
            except ValueError:
                print('Invalid input')
            else:
                break
        
        if userGuess == answer:
            display_separator(" ")
            print('CORRECT!')
            userScore += 1
            randomNumber_1 = None
            randomNumber_2 = None
            print('Score:', userScore)
            display_separator(' ')
        else:
            display_separator(" ")
            print('INCORRECT!')
            print('Answer:', answer)
            lives -= 1
            print(lives, 'lives left')
            display_separator(' ')
        
            if lives == 0:
                break
                
    if userScore == objective:
        print('Objective complete. Excellent work!')
    elif lives == 0:
        print('GAME OVER')
        print('Final score:', userScore)
    retry_display(2)


def select_multiplication():
    userScore = 0
    objective = settings.set_objective
    lives = settings.set_lives
        
    difficulty_display()
    
    while True:
        try:
            difficultyInput = int(input('Enter a difficulty: '))
        except ValueError:
                print('Invalid input')
        else:
            break
    
    difficulty = difficultyInput

    clear()
    while userScore < objective:
        if difficulty == 1:
            setValue.multiplicationNum_1 = 1
            setValue.multiplicationNum_2 = 10
            setValue.multiplicationNum_3 = 1
            setValue.multiplicationNum_4 = 5
            easyNum_1 = setValue.multiplicationNum_1
            easyNum_2 = setValue.multiplicationNum_2
            easyNum_3 = setValue.multiplicationNum_3
            easyNum_4 = setValue.multiplicationNum_4
            randomNumber_1 = randint(easyNum_1, easyNum_2)
            randomNumber_2 = randint(easyNum_3, easyNum_4)
        elif difficulty == 2:
            setValue.multiplicationNum_1 = 10
            setValue.multiplicationNum_2 = 30
            setValue.multiplicationNum_3 = 1
            setValue.multiplicationNum_4 = 10
            mediumNum_1 = setValue.multiplicationNum_1
            mediumNum_2 = setValue.multiplicationNum_2
            mediumNum_3 = setValue.multiplicationNum_3
            mediumNum_4 = setValue.multiplicationNum_4
            randomNumber_1 = randint(mediumNum_1, mediumNum_2)
            randomNumber_2 = randint(mediumNum_3, mediumNum_4)
        elif difficulty == 3:
            setValue.multiplicationNum_1 = 25
            setValue.multiplicationNum_2 = 80
            setValue.multiplicationNum_3 = 5
            setValue.multiplicationNum_4 = 25
            hardNum_1 = setValue.multiplicationNum_1
            hardNum_2 = setValue.multiplicationNum_2
            hardNum_3 = setValue.multiplicationNum_3
            hardNum_4 = setValue.multiplicationNum_4
            randomNumber_1 = randint(hardNum_1, hardNum_2)
            randomNumber_2 = randint(hardNum_3, hardNum_4)

        elif difficulty == 4:
            setValue.multiplicationNum_1 = 50
            setValue.multiplicationNum_2 = 150
            setValue.multiplicationNum_3 = 10
            setValue.multiplicationNum_4 = 40
            EXTREMENum_1 = setValue.multiplicationNum_1
            EXTREMENum_2 = setValue.multiplicationNum_2
            EXTREMENum_3 = setValue.multiplicationNum_3
            EXTREMENum_4 = setValue.multiplicationNum_4

            randomNumber_1 = randint(EXTREMENum_1, EXTREMENum_2)
            randomNumber_2 = randint(EXTREMENum_3, EXTREMENum_4)

        answer = randomNumber_1 * randomNumber_2
        
        print(randomNumber_1, "*", randomNumber_2)
        
        while True:
            try:
                userGuess = int(input(''))
            except ValueError: 
                print('Invalid input')
            else:
                break
        
        if userGuess == answer:
            display_separator(" ")
            print('CORRECT!')
            userScore += 1
            randomNumber_1 = None
            randomNumber_2 = None
            print('Score:', userScore)
            display_separator(' ')
        else:
            display_separator(" ")
            print('INCORRECT!')
            print('Answer:', answer)
            lives -= 1
            print(lives, 'lives left')
            display_separator(' ')

            if lives == 0:
                break
                
    if userScore == objective:
        print('Objective complete. Excellent work!')
    elif lives == 0:
        print('GAME OVER')
        print('Final score:', userScore)
    retry_display(3)


def select_devision():
    userScore = 0
    objective = settings.set_objective
    lives = settings.set_lives

    while True:
        try:
            difficultyInput = int(input('Enter a difficulty: '))
        except ValueError:
                print('Invalid input')
        else:
            break    

    difficulty_display()

    difficulty = difficultyInput

    clear()
    while userScore < objective:
        if difficulty == 1:
            setValue.divisionNum_1 = 6
            setValue.divisionNum_2 = 20
            setValue.divisionNum_3 = 2
            setValue.divisionNum_4 = 6
            easyNum_1 = setValue.divisionNum_1
            easyNum_2 = setValue.divisionNum_2
            easyNum_3 = setValue.divisionNum_3
            easyNum_4 = setValue.divisionNum_4            
            randomNumber_1 = randint(easyNum_1, easyNum_2)
            randomNumber_2 = randint(easyNum_3, easyNum_4)
        elif difficulty == 2:
            setValue.divisionNum_1 = 10
            setValue.divisionNum_2 = 40
            setValue.divisionNum_3 = 2
            setValue.divisionNum_4 = 10
            mediumNum_1 = setValue.divisionNum_1
            mediumNum_2 = setValue.divisionNum_2
            mediumNum_3 = setValue.divisionNum_3
            mediumNum_4 = setValue.divisionNum_4
            randomNumber_1 = randint(mediumNum_1, mediumNum_2)
            randomNumber_2 = randint(mediumNum_3, mediumNum_4)
        elif difficulty == 3:
            setValue.divisionNum_1 = 30
            setValue.divisionNum_2 = 60
            setValue.divisionNum_3 = 2
            setValue.divisionNum_4 = 12
            hardNum_1 = setValue.divisionNum_1
            hardNum_2 = setValue.divisionNum_2
            hardNum_3 = setValue.divisionNum_3
            hardNum_4 = setValue.divisionNum_4
            randomNumber_1 = randint(hardNum_1, hardNum_2)
            randomNumber_2 = randint(hardNum_3, hardNum_4)
        elif difficulty == 4:
            setValue.divisionNum_1 = 60
            setValue.divisionNum_2 = 150
            setValue.divisionNum_3 = 1
            setValue.divisionNum_4 = 16
            EXTREMENum_1 =  setValue.divisionNum_1
            EXTREMENum_2 =  setValue.divisionNum_2
            EXTREMENum_3 =  setValue.divisionNum_3
            EXTREMENum_4 =  setValue.divisionNum_4
            randomNumber_1 = randint(EXTREMENum_1, EXTREMENum_2)
            randomNumber_2 = randint(EXTREMENum_3, EXTREMENum_4)

        answer = randomNumber_1 // randomNumber_2

        print(randomNumber_1, "/", randomNumber_2)
        print(answer)

        while True:
            try:
                userGuess = int(input(''))
            except ValueError: 
                print('Invalid input')
            else:
                break
        
        if userGuess == answer:
            display_separator(" ")
            print('CORRECT!')
            userScore += 1
            randomNumber_1 = None
            randomNumber_2 = None
            print('score:', userScore)
        else:
            display_separator(" ")
            print('INCORRECT!')
            print('Answer:', answer)
            lives -= 1
            print(lives, 'lives left')
            display_separator(' ')
            
            if lives <= 0:
                break
                
    if userScore == objective:
        print('Objective complete. Excellent work!')
    elif lives == 0:
        print('GAME OVER')
        print('Final score:', userScore)
    retry_display(4)


def select_operator():
    operator_display()
    while True:
        userInput = input('Select an operator: ')
        
        if userInput == '1':
            display_separator(" ")
            print('You have selected addition')
            display_separator(" ")
            select_addition()

        elif userInput == '2':
            display_separator(" ")
            print('You have selected subtraction')
            display_separator(" ")
            select_subtraction()

        elif userInput == '3':
            display_separator(" ")
            print('You have selected multiplication')
            display_separator(" ")
            select_multiplication()

        elif userInput == '4':
            display_separator(" ")
            print('You have selected devision')
            display_separator(" ")
            select_devision()

        else:
            print('Invalid input')


def menu():
    clear()
    gamemode_display()
    while True:
        userInput = input('Select a gamemode: ')

        if userInput == '71':
            settings.set_objective = 999
            settings.set_lives = 999
            display_separator(' ')
            print('Developer mode activated')
            display_separator(' ')
            select_operator()

        elif userInput == '1': 
            settings.set_objective = 10
            settings.set_lives = 3
            display_separator(' ')
            print('You have selected 10 Questions')
            display_separator(' ')
            select_operator()

        elif userInput == '2':
            settings.set_objective = 25
            settings.set_lives = 3
            display_separator(' ')
            print('You have selected 25 Questions')
            display_separator(' ')
            select_operator()

        elif userInput == '3':
            settings.set_objective = 50
            settings.set_lives = 3
            display_separator(' ')
            print('You have selected 50 Questions')
            display_separator(' ')
            select_operator()
        
        elif userInput == '4':
            settings.set_objective = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            settings.set_lives = 1
            display_separator(' ')
            print('You have selected Rouge Mode')
            display_separator(' ')
            select_operator()

        elif userInput == '5':
            display_separator(' ')
            print('You have selected Custom Rules')
            display_separator(' ')
            custom_gamemode()

        else:
            print('Invalid input')


def main_display():
    title = 'Welcome to The Advanced Math Program (AMP).'
    print('-' * len(title))
    print(title)
    print('-' * len(title))
    print('For more information, enter "help" in the terminal.')
    display_separator(' ')

    while True:
        userInput = input('When you\'re ready, enter "start" to begin: ')
        if userInput == 'start':
            clear()
            menu()
        elif userInput == 'help':
            help_display()
        else:
            print('Invalid input')

main_display()