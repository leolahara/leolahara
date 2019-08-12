# assignment3.py
#
# Student name: Leola Hara
# Student id:  V00923578
import math     # imports Python's math library for your use (ie. math.sqrt)

THRESHOLD = 0.1 # to be used to compare floating point values

passed  = 0     # number of tests passed
tests   = 0     # number of tests run

def main():

    ''' Complete this assignment by doing the following for each function:
        - uncommenting one test function call in main
        NOTE: each test function has at least one test,
        but you should add additional tests where you feel necessary

        - implement the function (write the documentation and define the function)
        NOTE: follow the documentation provided for implementing each function
        in the assignment pdf

        - repeat until all functions are tested and implemented
        '''
    test_get_rectangle_area()
    test_get_average()
    test_append()
    test_distance()
    test_get_shipping_cost()




# implement each of the 5 functions after it's corresponding test function
# We have provided you with one test for each function
# You must add more to ensure you have consider all cases

def test_get_rectangle_area():
    result = get_rectangle_area(0,0)
    expected = 0
    print_test("get_rectangle_area", abs(expected-result)<THRESHOLD)

    result = get_rectangle_area(3.2,5.5)
    expected = 17.6
    print_test("get_rectangle_area", abs(expected-result)<THRESHOLD)

    result = get_rectangle_area(7.29,8.8)
    expected = 64.152
    print_test("get_rectangle_area", abs(expected-result)<THRESHOLD)
'''
    Purpose: design a function that takes two flaoting point numbers
             that represent length and width of a rectangle in cm and
             returns the area in cm squared.
    Arguements: length, width, (flaoting point numbers)
    Example: If length 3.2 and width 4.5, area returned would be 14.4
'''
def get_rectangle_area(length, width):
    area = length * width
    return area

# TODO: define get_rectangle_area...

def test_get_average():
    result = get_average(0,0,0)
    expected = 0
    print_test("get_average", abs(expected-result)<THRESHOLD)

    result = get_average(1.5,0.3,5.2)
    expected = 2.33333333
    print_test("get_average", abs(expected-result)<THRESHOLD)

    result = get_average(7.9,7.9,3.8)
    expected = 6.5333333
    print_test("get_average", abs(expected-result)<THRESHOLD)
'''
    Purpose: design a function that takes three flaoting point numbers
             and returns the average three numbers.
    Arguements: num1, num2, num3 (flaoting point numbers)
    Example: if num1 is 4.4, num2 is 5.5, num3 is 6.6, the returned value
             would be 5.5
'''
def get_average(num1, num2, num3):
    average = (num1 + num2 + num3)/ 3
    return average

# TODO: define get_average...

def test_append():
    result = append("", "")
    print_test("append", result == "")

    result = append("no way", "jose")
    print_test("append", result == "no wayjose")

    result = append("holy moly", "guacamole")
    print_test("append", result == "holy molyguacamole")
'''
    Purpose: design a function that takes two phrases and appends them into
             one new phrase and returns the new phrase with no space
             between the two phrases joined.
    Arguements: str1, str2 (both strings)
    Example: if str1 was 'you are' and str2 is 'awesome', the resulting string
             would be 'you areawesome'
'''
def append(str1, str2):
    phrase1 = str1
    phrase2 = str2
    append_1 = (str1.strip()+str2.strip())
    return append_1

# TODO: define append..

def test_distance():
    result = distance(3, 0, 0, 4)
    print_test("distance", abs(5-result)<THRESHOLD)

    result = distance(3, 5, 6, 8)
    print_test("distance", abs(2.8282427-result)<THRESHOLD)
'''
    Purpose: design a function called distance that takes four floating
                 point numbers as arguements that represent 2 points
                 and calculates and returns the distance between the two points.
    Arguements: x1, x2, y1, y2, (all floating point numbers)
    Example: if x1 = 2.2, x2= 4.2, y1= 8.4, y2= 9.1, the returned number
                 would be, 1.57797.....
'''
def distance(x1, x2, y1, y2):
    distance_1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance_1

# TODO: define distance...


def test_get_shipping_cost():
    std_len = 28.2
    std_wid = 10
    wt03 = 0.03

    result = get_shipping_cost(wt03, std_len, std_wid)
    expected = 1.05
    print_test("get_shipping_cost", abs(expected-result)<THRESHOLD)


    std_len = 10
    std_wid = 5
    wt03 = 0.06

    result = get_shipping_cost(wt03, std_len, std_wid)
    expected = 1.90
    print_test("get_shipping_cost", abs(expected-result)<THRESHOLD)
'''
    Purpose: design a function that takes the weight of the letter in kgs
             and the length and width of a letter in cm and calculates and
             returns the cost of shipping that letter.
    Arguements: weight, length, width (all floating point numbers)
    Example: if the weight is 0.24kg and the length is 12cm and width is 10cm
             it would be 1/90 + 1.4 * 0.5 = 2.6
'''
def get_shipping_cost(weight, length, width):
    area= get_rectangle_area(length, width)
    if (area <= 282 and weight <= 0.05):
        base_rate = 1.05
        if (weight <= 0.03):
            return(base_rate)
        else:
            return(1.05 + (((weight-.03)/.01) * .20))
    elif (weight <= 0.1):
        base_rate = 1.90
        return(base_rate)
    else:
            return(1.90 + (((weight - 0.1)/0.1) * 0.50))



    # if (area < 282 and wt03 < 0.05):
    #     print(1.05 +((wt03 > 0.03)/ 10) * 20 )
    # else:
    #     print(1.90 +((wt03 > 0.1)/ 100) * 50 )
    # return get_shipping_cost
# TODO: define get_shipping_cost...



''' Purpose:
        prints test_name followed by "passed" if expression evaluates to True,
        prints test_name followed by "failed" if expression evaluates to False
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
