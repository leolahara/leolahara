# assignment2.py
#
# Student name: Leola Hara
# Student id: V00923578

def main():
    print('Assignment 2')
    ''' Complete this assignment by doing the following for each function:
        - uncommenting one test function call in main
        NOTE: each test function has at least one test,
        but you should add additional tests where you feel necessary

        - implement the function (write the documentation and define the function)
        NOTE: follow the documentation provided for implementing each function
        in the assignment pdf

        - repeat until all functions are tested and implemented
        '''
    test_print_dog_years()
    test_print_average()
    test_is_speeding()
    test_print_as_question()
    test_print_max()
    test_print_test()

    ''' #Purpose: take an integer that represents a dog's age in human years
        #and print the dog's age in dog years

        #Arguements: human_years (integer)

        #Example: if human_years is 5, dog years will be ('human_years' * 7)
        #which gives us 35.
    '''
def test_print_dog_years():
    print_dog_years(0)  #expects 0
    print_dog_years(4)  #expects 28
    print_dog_years(8)  #expects 56
    print_dog_years(10) #expects 70
    print_dog_years(20) #expects 140

# TODO: define print_dog_years...
def print_dog_years (human_years):
    dog_years = (human_years * 7)
    if (human_years >= 0):
        print("In human years the dog would be", human_years, "years old, but in dog years the dog would be", dog_years, "years old")
    else:
        print("Dog years not defined")


        ''' #Purpose:design a function that takes three flaoting point numbers
            #and takes the average of those three numbers.

            #Arguements: three_floating_numbers (all floats)

            #Example: if i were to have three flaoting point numbers;
            # 3.3, 4.4, and 5,5, the function would print, 4.4.
        '''
def test_print_average():
    print_average(0,0,0)          #expects 0
    print_average(1.2, 2.2, 3.2)  #expects 2.2
    print_average(3.3,4.3,5.3)    #expects 4.3
    print_average(4.5,5.5,6.5)    #expects 5.5

# TODO: define print_average...
def print_average(flaot1,flaot2,flaot3):
    average = ((flaot1 + flaot2 + flaot3) / 3)
    print(average)


    ''' #purpose: print a function that takes an integer that represents
        #the speed of a car in km/hr and an integer representing the speed limit in km/hr

        #arguements: speed(int), speed_limit(int), X(int)

        #example: if the speed was 90 and the speed limit was 100, the function would print,
        # you are 10km/hr below legal speed.
    '''
def test_is_speeding():
    is_speeding(90, 100)    #expects: 'you are 10km/hr below legal limit'
    is_speeding(80, 120)    #expects: 'you are 40km/hr below legal limit'
    is_speeding(70, 90)     #expects: 'you are 20km/hr below legal limit'
    is_speeding(120, 40)    #expects: 'Slow down! you are going 120km/hr'
    is_speeding(200, 180)   #expects: 'Slow down! you are going 200km/hr'

# TODO: define is_speeding...
def is_speeding(speed, speed_limit):
    X = (speed_limit - speed)
    if  (speed > speed_limit):
        print('Slow down! You are going', speed, 'km/hr')
    elif  (speed < speed_limit):
        print('You are going', X ,'km/hr below legal limit')
    elif  (speed == speed_limit):
        print('You are driving at the legal limit.')


        ''' #purpose: design a function that takes a phrase and prints that phrase
            #with a question mark at the end if it's not already there

            #arguements:phrase(string)

            #example: if the phrase was why, the function would add a question mark to it,
            #making it 'why?'
        '''
def test_print_as_question():
    print_as_question('')           #expects: '?'
    print_as_question('why')        #expects: 'why?'
    print_as_question('are you ok') #expects: 'are you ok?'
    print_as_question('how old are you') #expects: 'how old are you?'
    print_as_question('do you like apples') #expects: 'do you like apples?'

# TODO: define print_as_question...
def print_as_question(phrase):
    if ('?'in phrase):
        print(phrase)
    elif ('?' not in phrase):
        question = (phrase + '?')
        print(question)


        ''' #purpose: to design a function that takes three flaoting point three_floating_numbers
            # and prints the biggest of the three values

            #arguements:num1(flaot), num2(flaot), num3(flaot)

            #example: if i were to have three flaoting numbers; 1.1, 2.2, and 3.3,
            #the function would print 3.3, which is the largest of the three numbers.
        '''
def test_print_max():
    print_max(0,0,0)            #expect 0
    print_max(1.1, 2.2, 3.3)    #expect: 3.3
    print_max(2.2, 3.3, 4.4)    #expect: 4.4
    print_max(5.5, 2.4, 9.7)    #expect: 9.7
    print_max(2.2, 4.3, 1.1)    #expect: 4.3

# TODO: define print_max...
def print_max(x, y, z):
    if (x > y and x > z):#(x > y and z)
        print(x)
    elif (y > x and y > z):
        print(y)
    else:
        print(z)


        '''#purpose: to design a function that takes a phrase and a boolean expression
           #as arguements.

           #arguements: statement_1(string), statement_2(int)

           #example:if i wanted to pass the boolean expression, i would enter a true statement,
           #such as 8==8. if i wanted to fail the boolean expression, i would enter a false statement,
           #such as 3==4.
        '''
def test_print_test():
    print_test("not pass int", 3==4)                #expect "not pass int : failed"
    print_test("not pass int", 5==3)
    print_test("not pass int", 9==1)
    print_test("pass int", 8==8)
    print_test("pass int", 7==7)

# TODO: define print_test...
def print_test(statement_1, statement_2):
    if (statement_2 is True):
        print("pass int: passed")
    else:
        print("not pass int: failed")


# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
