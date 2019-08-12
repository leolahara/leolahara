# assignment10.py
#
# Student name:Leola Hara
# Netlink id:  V00923578

passed = 0
tests = 0

import Date as dt

''' This assignment requires you to complete functions within the Date class (Date.py)
    and other functions that use the Date class within assignment10.py

    Complete this assignment by doing the following for each function:
    - uncommenting one test function call in main
    NOTE: each test function tests one of the functions you must write,
          some access instance dt.Date, while others do not

    - implement the function (define the function)
    NOTE: follow the documentation provided here for implementing each function


    '''

def main():
    print('Assignment 10')
    test_is_leap_year()
    test_is_before()
    test_get_years()
    test_get_leap_years()
    print(passed, '/', tests, ' tests passed')

def test_is_leap_year():
    d1LeapYear = dt.Date(1,1,2008)
    d2LeapYear = dt.Date(3,23,2000)

    d1NotLeapYear = dt.Date(1,1,1582)
    d2NotLeapYear = dt.Date(3,23,1900)
    d3NotLeapYear = dt.Date(3,23,2009)
    d4NotLeapYear = dt.Date(2,23,2010)
    d5NotLeapYear = dt.Date(2,23,2011)

    print_test('test_is_leap_year 2008 - true', d1LeapYear.is_leap_year())
    print_test('test_is_leap_year 2000 - true', d2LeapYear.is_leap_year())

    print_test('test_is_leap_year 1582 - false', not(d1NotLeapYear.is_leap_year()))
    print_test('test_is_leap_year 1900 - false', not(d2NotLeapYear.is_leap_year()))
    print_test('test_is_leap_year 2009 - false', not(d3NotLeapYear.is_leap_year()))
    print_test('test_is_leap_year 2010 - false', not(d4NotLeapYear.is_leap_year()))
    print_test('test_is_leap_year 2011 - false', not(d5NotLeapYear.is_leap_year()))

def test_is_before():
    d1a         = dt.Date(3,23,2018)
    d1Same      = dt.Date(3,23,2018)
    d1Before1a  = dt.Date(3,23,2017)
    d2Before1a  = dt.Date(2,23,2018)
    d3Before1a  = dt.Date(3,22,2018)

    d1After1a   = dt.Date(3,24,2018)
    d2After1a   = dt.Date(4,22,2018)
    d3After1a   = dt.Date(4,22,2019)
    d4After1a   = dt.Date(2,24,2019)
    d5After1a   = dt.Date(2,21,2019)

    print_test('test_is_before- different objects, equal dt.Date', not(d1Same.is_before(d1a)))
    print_test('test_is_before - different objects, equal dt.Date', not(d1a.is_before(d1Same)))

    print_test('test_is_before - year is before', d1Before1a.is_before(d1a))
    print_test('test_is_before - month is before', d2Before1a.is_before(d1a))
    print_test('test_is_before - day is before', d3Before1a.is_before(d1a))

    print_test('test_is_before - day is after', not(d1After1a.is_before(d1a)))
    print_test('test_is_before - month is after', not(d2After1a.is_before(d1a)))
    print_test('test_is_before - year is after, day is not', not(d3After1a.is_before(d1a)))
    print_test('test_is_before - year is after, month is not', not(d4After1a.is_before(d1a)))
    print_test('test_is_before - year is after, month and day are not', not(d5After1a.is_before(d1a)))


def test_get_years():
    empty = []
    result = get_years(empty)
    print_test('test_get_years empty', result == [])

    d0 = dt.Date(2,23,2011)
    d1 = dt.Date(3,23,1900)
    d2 = dt.Date(3,23,2009)
    d3 = dt.Date(2,23,2010)

    dt.Dates4 = [d0, d1, d2, d3]
    result = get_years(dt.Dates4)
    print_test('test_get_years not empty', result == [2011, 1900, 2009, 2010])

''' Purpose:
        creates a newlist of the years of each element in dt.Dates
    Args:
        dt.Dates (list): a list of valid dt.Dates
    Returns:
        (list): newlist of years as ints
    '''
    # TODO: define get_years...
def get_years(dates):

    new_list = []
    for birthdays in dates:
        new_list.append(birthdays.get_year())

    return new_list



def test_get_leap_years():
    empty = []
    result = get_leap_years(empty)
    print_test('test_get_leap_years', result == [])

    d1LeapYear = dt.Date(1,1,2008)
    d2LeapYear = dt.Date(3,23,2000)

    d0NotLeapYear = dt.Date(3,23,2009)
    d1NotLeapYear = dt.Date(1,1,1582)
    d2NotLeapYear = dt.Date(3,23,1900)

    all_leap_years = [d1LeapYear, d2LeapYear]
    result = get_leap_years(all_leap_years)
    print_test('test_get_leap_years', result == [d1LeapYear, d2LeapYear])

    no_leap_years = [d0NotLeapYear, d1NotLeapYear, d2NotLeapYear]
    result = get_leap_years(no_leap_years)
    print_test('test_get_leap_years', result == [])

    some_leap_years = [d0NotLeapYear, d2LeapYear, d1NotLeapYear, d2NotLeapYear, d1LeapYear]
    result = get_leap_years(some_leap_years)
    print_test('test_get_leap_years', result == [d2LeapYear, d1LeapYear])

''' Purpose:
        creates a newlist of dt.Date of only those from dt.Dates that are leap years
    Args:
        dt.Dates (list): a list of valid dt.Dates
    Returns:
        (list): newlist of dt.Dates that are leap years
    '''
    # TODO: define get_leap_years...
def get_leap_years(dates):
    new_list = []
    for birthday in dates:
        if birthday.is_leap_year() == True:
            new_list.append(birthday)


    return new_list




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
