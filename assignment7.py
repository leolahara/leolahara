import matplotlib.pyplot as plotter
# assignment7.py
#
# Student name: Leola Hara
# Netlink id: V00923578

passed = 0
tests = 0

''' Complete this assignment by doing the following for each function:
    - uncommenting one test function call in main
    NOTE: each test function has at least one test,
    but you should add additional tests where you feel necessary

    - implement the function (define the function)
    NOTE: follow the documentation provided here for implementing each function

    - repeat until all functions are tested and implemented

    NOTE: you may not use Python built-in libraries for list operations with the exception of append and for with in operator (ie. for num in listâ€¦)
    '''
def main():
    print('Assignment 7')
    test_multiply_by()
    test_is_sorted()
    test_shift_left()
    test_count_occurrences ()
    test_get_vals()
    test_draw_line_graph()


    print(passed, '/', tests, ' tests passed')

def test_multiply_by():
    emptylist = []
    multiply_by(emptylist, 4)
    print_test('multiply_by emptylist and 2', emptylist==[])

    list1 = [6]
    multiply_by(list1, 4)
    print_test('multiply_by list1 and 4', list1==[24])

    list2 = [5]
    multiply_by(list2, 3)
    print_test('multiply_by list2 and 3', list2==[15])

    list3 = [7,6,5]
    multiply_by(list3, 7)
    print_test('multiply_by list3 and 7', list3==[49,42,35])

    list4 = [1,-2,0,4,-5]
    multiply_by(list4, 2)
    print_test('multiply_by list4 and 2', list4==[2,-4,0,8,-10])

''' Purpose:
        multiplies all values in numbers by multiplier
    Args:
        numbers (list): the list of integers
        multiplier (int): the number to mutiply by
    '''
# TODO: define multiply_by here...
def multiply_by(numbers, multiplier):
    index = 0
    for num in numbers:
        numbers[index] = num * multiplier
        index += 1






def test_is_sorted():
    emptylist = []
    result = is_sorted(emptylist)
    print_test('test_is_sorted emptylist', result==True)

    list1 = [6]
    result = is_sorted(list1)
    print_test('test_is_sorted list1', result==True)

    list4_sorted = [1, 9, 4, 5]
    result = is_sorted(list4_sorted)
    print_test('test_is_sorted list4_sorted', result==False)

    list5_sorted = [2,-3,4,5]
    result = is_sorted(list5_sorted)
    print_test('test_is_sorted list5_sorted', result==False)

    list6_sorted = [-4,9,10,11]
    result = is_sorted(list6_sorted)
    print_test('test_is_sorted list6_sorted', result==True)

    list7_sorted = [-9,8,4,7]
    result = is_sorted(list7_sorted)
    print_test('test_is_sorted list7_sorted', result==False)

    list8_sorted = [1,2,3,4]
    result = is_sorted(list8_sorted)
    print_test('test_is_sorted list8_sorted', result==True)

''' Purpose:
        determines whether values in the list numbers
        are sorted in increasing order
    Examples:
        [] is in increasing sorted order
        [1, 2, 2, 5] is in increasing sorted order
        [1, 2, 2, 0] is not in increasing sorted order
    Args:
        numbers (list): the list of numbers
    Returns:
        (bool): True if sorted, False otherwise
    '''
# TODO: define is_sorted here...
def is_sorted(numbers):
    index = 0
    increasing = True
    for val in numbers[0:-1]:
        comparing = numbers[index+1]
        if val<= comparing:
            increasing = True
            index = index + 1
        else:
            return False

    return increasing






def test_shift_left():
    emptylist = []
    result = shift_left(emptylist, 2)
    print_test('test_shift_left emptylist', result==[])

    list1 = [6]
    result = shift_left(list1, 2)
    print_test('test_shift_left list1 by 2', result==[6])

    list4a = [1, 4, 7, 5]
    result = shift_left(list4a, 1)
    print_test('test_shift_left list4a by 1', result==[4, 7, 5, 1])

    list4b = [1, 4, 7, 5]
    result = shift_left(list4b, 2)
    print_test('test_shift_left list4b by 2', result==[7,5,1,4])

    list4c = [1,2,3,4]
    result = shift_left(list4c, 3)
    print_test('test_shift_left list4c by 3', result==[4,1,2,3])

    list4d = [1,2,3,4]
    result = shift_left(list4c, 3)
    print_test('test_shift_left list4d by 3', result==[4,1,2,3])

    list4e = [5,7,9,2]
    result = shift_left(list4e, 2)
    print_test('test_shift_left list4e by 2', result==[9,2,5,7])

''' Purpose:
        copies every value in elements into a new list
        where the position of every value is shifted
        to the left by the specified amount
    Args:
        elements (list): the list of elements to shift
        shiftby (int): the amount to shift the values by
    Returns:
        (list): the new list with values shifted
    '''
# TODO: define shift_left here...
def shift_left(elements, shiftby):
    new_list = elements[shiftby:] + elements[:shiftby]

    return new_list






def test_count_occurrences ():
    emptylist = []
    result = count_occurrences (emptylist, 2)
    print_test('test_count_occurrences  emptylist', result==0)

    list_numbers = [1, 3, 1, 4, 5, 7, 3, 1]
    result = count_occurrences (list_numbers, 1)
    print_test('test_count_occurrences  list_numbers 1', result==3)

    list_words = ['hi', 'bye', 'hi', 'hi']
    result = count_occurrences (list_words, 'hi')
    print_test('test_count_occurrences  list_numbers \'hi\'', result==3)

    list_mynums = [1,3,5,7,9]
    result = count_occurrences (list_mynums, 5)
    print_test('test_count_occurrences list_numbers 5', result==1)

    list_of_nums = [2,2,3,4,5,-6]
    result = count_occurrences (list_of_nums, 2)
    print_test('test_count_occurrences list_of_nums 2', result==2)

    list_of_words = ['leola', 'ethan', 'reina', 'ethan']
    result = count_occurrences (list_of_words, 'ethan')
    print_test('test_count_occurrences list_of_words \'ethan\'', result ==2)

''' Purpose:
        counts the occurrences  of looking_for in elements
    Args:
        elements (list): the list of elements
        looking_for (type of values in elements): value being counted
    Returns:
        (int): the count
    '''
# TODO: define count_occurrences  here...

def count_occurrences(elements, looking_for):
    count = 0
    for val in elements:
        if val == looking_for:
            count += 1

    return count








def test_get_vals():
    emptylist = []
    result = get_vals(emptylist, 0)
    print_test('test_get_vals emptylist', result==[])

    list_4_tuples_len_2 = [(1,2), (4,5), (8,9), (-1,7)]
    result = get_vals(list_4_tuples_len_2, 0)
    print_test('test_get_vals list_4postions, 0', result==[1,4,8,-1])

    result = get_vals(list_4_tuples_len_2, 1)
    print_test('test_get_vals list_4_tuples_len_2, 1', result==[2,5,9,7])


    list_4_tuples_len_3 = [('dog', 'Rover' ,2), ('cat', 'Clyde' ,3),
                           ('pig', 'Wilbur' ,1), ('dog', 'Scout' ,4)]
    result = get_vals(list_4_tuples_len_3, 0)
    print_test('test_get_vals list_4_tuples_len_3, 0', result==['dog', 'cat', 'pig', 'dog'])


''' Purpose:
        create a new list of values from the given position
        in the list of tuples
    Examples:
        if elements is [(1,2),(3,4)] and position is 0
            the new list will be [1,3]
        if elements is [(1,2,3),(4,5,6)] and position is 2
            the new list will be [3,6]
    Precondition:
        position is >=0 and < length of every tuple in elements
    Args:
        elements (list of tuples): the list of elements
        position (int): the position of the value in the tuple
    Returns:
        (list): the new list with values
    '''
# TODO: define get_vals here...
def get_vals(elements, position):
    new_list = []
    for tuple in elements:
        val = tuple[position]
        new_list.append(val)

    return new_list






def test_draw_line_graph():
    emptylist_postions = []
    draw_line_graph(emptylist_postions)

    list_4postions = [(-1,7), (1,2), (4,6), (8,9)]
    draw_line_graph(list_4postions)

    list_5postions = [(5,2), (9,3), (4,5), (7,1)]
    draw_line_graph(list_5postions)

    list_6postions = [(1,4), (2,5), (3,6)]
    draw_line_graph(list_6postions)

    list_7postions = [(9,1), (2,4), (4,7), (5,8)]
    draw_line_graph(list_7postions)

''' Purpose:
        given a list_of_positions get:
        the corresponding list of x values in list_of_positions and
        the corresponding list of y values in list_of_positions
        and use them to plot a line graph
    Args:
        list_of_positions (list): the list of tuples with x,y values (int,int)
    '''
# TODO: define draw_line_graph here...
# HINT: this is only a few lines of code but you will need to use the functions
#  plot_positions and get_vals
def draw_line_graph(list):
    x_value = get_vals(list, 0)
    y_value = get_vals(list, 1)

    list = plot_positions(x_value, y_value)



''' Purpose:
        plot a line graph using xcoords and ycoords
    Precondition:
        lengths of xcoords and ycoords must be equal
    Args:
        xcoords (list): the list of x coordinates
        ycoords (list): the list of y coordinates
    '''
def plot_positions(xcoords, ycoords):
    plotter.plot(xcoords, ycoords)
    plotter.show()


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
