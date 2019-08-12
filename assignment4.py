# assignment4.py
#
# Student name:Leola Hara
# Student id: V00923578

def main():
    print('Assignment 4')
    ''' Complete this assignment by doing the following for each function:
        - uncommenting one test function call in main
        NOTE: each test function has at least one test,
        but you should add additional tests where you feel necessary

        - implement (define) the function
        NOTE: follow the documentation provided for implementing each function
             (in the assignment pdf and the function documentation)

        - repeat until all functions are tested and implemented

        You are free to write additional helper functions but
        you MUST have at least the functions specified and
        they must do exactly as specified
        '''
    # test_sum_odd()
    # test_draw_space_craft()
    # test_draw_lem_adapter()
    # test_draw_instrument_unit()
    # test_draw_booster()
    # test_draw_tail()
    test_draw_rocket()


def test_sum_odd():
    result = sum_odd(0)
    expected = 0
    print(result)
    print_test("sum_odd", expected == result)

    result = sum_odd(3)
    expected = 4
    print(result)
    print_test("sum_odd", expected == result)

    result = sum_odd(5)
    expected = 9
    print(result)
    print_test("sum_odd", expected == result)

    result = sum_odd(7)
    expected = 16
    print(result)
    print_test("sum_odd", expected == result)

''' Purpose:
        calculate the sum of the odd values
        from 0 to n inclusive
    Args:
        n (int): the upper limit to sum up to
    Returns:
        (int): the sum
    '''
# TODO: define sum_odd...
def sum_odd(n):
    sum = 0
    # if (n%2==0):
    #     print(0)
    # elif (n%2==1):
    for nums in range(1, n+1, 2):
        sum += nums
    return(sum)




def test_draw_space_craft():
    result = draw_space_craft(3)

''' Purpose:
        prints a space craft with width and height
        relative to size
    Args:
        size (int): size of the spacecraft
    Prints: space craft with size (int)
'''
# TODO: define draw_space_craft...
def draw_space_craft(size):

    for row in range (size * 2):
        print(' ', end='')
        print(' '*(size*2 - row), end = ' ')

        for col in range (row):
            print('/', end = '')

        print('**',end = '')

        for col in range (row):
            print('\\', end = '')

        for col in range (row):
            print(' ', end = '')

        print('')

    print(' ', end = '')
    print(' ', end = '')
    print('+', end='')
    print(('=*' * (2*size)), end = '')
    print('+')




def test_draw_lem_adapter():
    draw_lem_adapter(4)

''' Purpose:
        prints a the lem adapter with width
        relative to size
    Args:
        size (int): size of lem adapter
    Print: lem adapter with width relative to size (int)
    '''
# TODO: define draw_lem_adapter...
def draw_lem_adapter(size):
    for row in range (1):
        print(' ', end='')

        for col in range (row+1):
            print('//', end = '')

        print(' %' * (size * 2), end='')

        for col in range (row+1):
            print('\\\\', end = '')

        for col in range (row):
            print(' ', end='')

    for row in range(1):
        print(' ')

        for col in range (row+1):
            print('//', end = '')

        print(' %' * (size * 2 + 1),end = '')

        for col in range (row+1):
            print('\\\\', end = '')

        for col in range (row):
            print(' ', end='')

        print('')

    print('+', end='')
    print(('=*' * (2*size + 2)), end = '')
    print('+')




def test_draw_instrument_unit():
    draw_instrument_unit(4)

''' Purpose:
        prints a the instrument unit with width
        relative to size
    Args:
        size (int): size of lem adapter
    Prints:
        prints instrument unit with width relative to size (int)
    '''
# TODO: define draw_instrument_unit...
def draw_instrument_unit(size):
    for row in range (1):
        print('', end='')

        for col in range (row+1):
            print('||', end = '')

        print('~#' * (size * 2+1), end='')

        for col in range (row+1):
            print('||', end = '')

        for col in range (row):
            print(' ')

    for row in range (1):
        print('')

        for col in range (row+1):
            print('||', end = '')

        print('~#' * (size * 2+1), end='')

        for col in range (row+1):
            print('||')

        for col in range (row):
            print(' ', end='')

    print('+', end='')
    print(('=*' * (2*size + 2)), end = '')
    print('+')

    print('', end='')



def test_draw_booster():
    draw_booster(4,3)

''' Purpose:
        prints a the booster with height and width
        relative to size
    Args:
        size (int): size of booster
        n (int): how many times it repeats the boosters
    Print: a booster relative to height and width relative to size (int)
             and booster (how many times it wants to repeat it)
    '''
# TODO: define draw_booster...
def draw_booster(size, booster):
    for booster in range (booster):
        for row in range(size+1):
            print('|', end='')
            print('.'*(size-row), end='')
            print('/\\'*(row+1), end='')
            print('..'*(size-row), end='')
            print('/\\'*(row+1), end='')
            print('.'*(size-row), end='')
            print('|')

        for row in range(size+1):
            print('|', end='')
            print('.'*(row), end='')
            print('\\/'*(size-row+1), end='')
            print('..'*(row), end='')
            print('\\/'*(size-row+1), end='')
            print('.'*(row), end='')
            print('|')


    print('+', end='')
    print(('=*' * (2*size + 2)), end = '')
    print('+')

    print('', end='')


def test_draw_tail():
    draw_tail(4)

''' Purpose:
        prints a the tail with width
        relative to size
    Args:
        size (int): size of booster
    Prints: the tail relative to size (int)
    '''
# TODO: define draw_tail...
def draw_tail(size):
    for row in range(1):
        print('//  ', end='')

        # for col in range(1):
        print('/\\  ' * size, end='')
        print('\\\\', end='')



def test_draw_rocket():
    draw_rocket(4,3)

''' Purpose:
        prints a rocket of given size with n boosters
    Args:
        size (int): size of rocket
        n (int): number of boosters
    '''
# TODO: define draw_rocket..
def draw_rocket(size, booster):
    draw_space_craft(size)
    draw_lem_adapter(size)
    draw_instrument_unit(size)
    draw_booster(size, booster)
    draw_tail(size)

    print('', end='')

''' Purpose:
        prints test_name followed by ": passed" if expression evaluates to true,
        prints test_name followed by ": failed" if expression evaluates to false
    Args:
        test_name (str): the name of the test
        expression (bool): a boolean expression'
    '''
def print_test(test_name, expression):
    if(expression):
        print(test_name + ': passed')
    else:
        print(test_name + ': failed')

# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
