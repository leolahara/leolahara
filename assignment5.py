# assignment5.py
#
# Student name:Leola Hara
# Netlink id: V00923578

from random import randint
MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5

passed = 0
tests = 0

''' Complete this assignment by doing the following for each function:
        - uncommenting one test function call in main one at a time
          NOTE: each test function has suggestions for testing
        - implement the function that test is testing
          NOTE: follow the documentation for implementing each function
        - when you are done, comment out the test function call
        - repeat until all functions are tested and implemented
        '''
def main():
    print('Assignment 5')
    #test_get_bet()
    #test_play_again()
    #test_compute_winnings()
    #test_get_guess()
    #test_playround()
    test_playgame()


''' Purpose:
        simlulates the roll of 3 dice
        returns the count of the dice rolls that == guess
    Args:
        guess (int): the player's guess

    Returns:
        count (int): the dice roll == guess
    '''
# we defined this function for you to use
def roll_dice(guess):
    die1 = randint(MIN_ROLL,MAX_ROLL)
    die2 = randint(MIN_ROLL,MAX_ROLL)
    die3 = randint(MIN_ROLL,MAX_ROLL)

    print('Dice rolls: ', die1, ' ', die2, ' ', die3);

    result = 0

    if (die1 == guess):
        result += 1

    if (die2 == guess):
        result += 1

    if (die3 == guess):
        result += 1

    return result;




def test_get_bet():
    result = get_bet(300)
    print(result)
    # value of result will be dependant on what is given for user input
    # try enough inputs (valid and invalid) to test all possible paths through the function

''' Purpose:
        Prompts the user for the amount of money they want to bet
        Values entered that are not a integer or that are
        less than MIN_BET or higher than bankroll are considered invalid entries.
        Continues to prompt the user until a valid amount is entered.
    Args:
        bankroll (int): the amount of money the user has to play with

    Returns:
        money (int): amount of user's bet
'''
# TODO: define the get_bet function here:
def get_bet(bankroll):
    print('Hello, you have $', bankroll, 'to play with.')
    bet = input('Enter the amount you want to bet: ')

    invalid_input = True
    while invalid_input:
        if bet.isdigit():
           bet = int(bet)
           if (bankroll==0 or bankroll<5):
               bet = input('You do not have enough money to bet \n0')
           if not (MIN_BET<=bet<=bankroll):
                bet = input('Please enter an amount equal to or above 5 dollars and below your bankroll: ')
           elif (bet>=MIN_BET) or (bet>bankroll):
                invalid_input = False
        else:
            bet = input('Please enter a valid input as a int, not a string or flaot: ')

    return(bet)






def test_play_again():
    result = play_again()
    print(result)
    # value of result will be dependant on what is given for user input
    # try 'yes' input (result shoule be True) and an input not 'yes' (result should be False)

''' Purpose:
        Prompts the user to determine whether they want to play again.
        user enters 'yes' if they want to play again, any other entry
        means they don't want to play again

    Returns:
        again (boolean): True if user wants to play again, false otherwise
    '''
# TODO: define the play_again function here:
def play_again():
    playings=input('Do you want bet? Enter yes if you want to, no if you do not: ')
    while True:
        if (playings == 'yes' or playings == 'YES' or playings == 'Yes'
        or playings == 'YEs' or playings == 'YeS' or playings == 'yES'):
            again = True
            return again
        else:
            again = False
            return again






def test_compute_winnings():
    result = compute_winnings(0, 50)
    print_test('test_compute_winnings 0 matches and $50', result == -50)

    result = compute_winnings(1, 150)
    print_test('test_compute_winnings 1 match and $150', result == 150)

    result = compute_winnings(2, 30)
    print_test('test_compute_winnings 2 matches and $30', result == 60)

    result = compute_winnings(3, 25)
    print_test('test_compute_winnings 3 matches and $25', result == 250)

''' Purpose:
        returns the amount the user has won (a positive number),
        or lost (a negative number)
        The amount is based on the following odds:
        0 dice matching player loses their whole bet
        1 dice matching, player gets 1:1 odds on their bet
        2 dice matching player gets 2:1 odds on their bet
        3 dice matching player gets 10:1 odds on their bet

    Args:
        num_matches (int): the number of matching dice
        bet(int):  the amount of the bet

    Precondition:
        num_matches is 0,1,2 or 3

    Returns:
        amount (int): the amount of money won/lost
    '''
# TODO: define the compute_winnings function here:
def compute_winnings(dice_matching, bet):
    if (dice_matching ==0):
        amount = 0 - bet
    elif (dice_matching ==1):
        amount = bet * 1
    elif (dice_matching ==2):
        amount = bet * 2
    elif (dice_matching ==3):
        amount = bet * 10
    elif (dice_matching<=4 or dice_matching<0):
        amount =(input('invalid amount'))

    return amount






def test_get_guess():
    result = get_guess()
    print(result)
    print_test('test_get_guess, should be a number 1-6', result>=1 and result <=6)
    # value of result will be dependant on what is given for user input
    # try enough inputs (valid and invalid) to test all possible paths through the function

''' Purpose:
        repeatedly prompts the user for a valid guess
        an invalid guess is something that is not a whole number
        or a number smaller than 1 or bigger than 6

    Returns:
        guess (int): the valid guess
    '''
# TODO: define the get_guess function here:
def get_guess():
    guess = input('Please choose a number between 1 and 6: ')
    invalid_input = True
    while invalid_input:
        if guess.isdigit():
           guess = int(guess)

           if not(guess==1 or guess==2 or guess==3 or guess==4 or guess==5 or guess==6):
               guess = input('Please enter a valid input between 1 and 6: ')
           else:
               invalid_input = False
        else:
            guess = input('Please enter a valid input as a int between 1 and 6; not a string or flaot: ')

    return int(guess)






def test_playround():
    result = playround(40)
    #print(result)
    # value of result will be dependant on what is given for user input
    # play enough round to test all possible paths through the function

''' Purpose:
        plays one round of the dice game:
        -gets the user's guess
        -rolls the dice
        -computes the amount of money won/lost
        returns the amount won/lost.
        -a positive amount means they won
        -a negative amount means they lost
    Args:
        bet (int): the amount the user is betting
    Returns:
        amount (int): the amount of money won/lost
    '''
# TODO: define the playround function here:
def playround(bet):
    guess = get_guess()
    dice_matching = roll_dice(guess)
    compute_winnings(dice_matching, bet)
    amount = compute_winnings(dice_matching, bet)

    if (amount<bet):
        print('I am sorry, you lost $', abs(amount))
    else:
        print('Congratulations! You won $', amount)

    return amount






def test_playgame():
    # result = playgame(0)
    # print(result)
    # 0 bet is < MIN_BET so it should not let you play
    result = playgame(500)
    print(result)
    # value of result will be dependant on what is given for user input

''' Purpose:
        continually allows the user to playrounds of the game
         while their bankroll is at least MIN_BET and
         they still want to play again
        allows the user to play a round of the game
        prints the amount won or lost in the round
        updates the bankroll based on the amount won or lost
    Args:
        bankroll (int): the initial amount to play the game with
    Returns:
        bankroll (boolean): True if user wants to play again, False otherwise
    '''
# TODO: define the playgame function here:
def playgame(bankroll):
    valid_input = True
    while valid_input:
        decision = play_again()
        if decision==True and (bankroll>=MIN_BET):
            bet = get_bet(bankroll)
            amount = playround(bet)
            bankroll += amount
        else:
            valid_input = False

    return bankroll






''' Purpose:
        prints test_name followed by ': passed' if expression evaluates to true,
        prints test_name followed by ': failed' if expression evaluates to false
    Args:
        test_name (str): the name of the test
        expression (bool): a boolean expression'
    '''
def print_test(test_name, expression):
    global tests
    global passed
    tests += 1
    if(expression):
        print(test_name + ': passed')
        passed += 1
    else:
        print(test_name + ': failed')


# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
