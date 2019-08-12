# assignment6.py
#
# Student name: Leola Hara
# Student id:  V00923578

passed = 0
tests = 0

''' Complete this assignment by doing the following for each function:
    - uncommenting one test function call in main
    NOTE: each test function has at least one test,
    but you should add additional tests where you feel necessary

    - implement the function (define the function)
    NOTE: follow the documentation provided here for implementing each function

    - repeat until all functions are tested and implemented
    '''

def main():
    print('Assignment 6')
    test_print_double()
    test_multiply_by()
    test_get_above()
    test_sum_odd()
    test_get_min()
    test_contain_negative()

    print(passed, '/', tests, ' tests passed')

def test_print_double():
    emptylist = []
    print_double(emptylist)
    print_test('test_print_double emptylist', emptylist==[])

    my_list = [1,2,3]
    print_test('test_print_double my_list', my_list==[1,2,3])

    list1 = [2,4,6,8]
    print_test('test_print_double list1', list1==[2,4,6,8])

    list2 = [1,2,3,4,5]
    print_test('test_print_double list2', list2==[1,2,3,4,5])

''' Purpose:
        prints every value in numbers doubled
        numbers is not changed
    Args:
        numbers (list): the list of numbers
    '''
# TODO: define print_double here...
def print_double(list):
    for num in list:
        num *= 2
        print(num, sep=' ', end= '')


        # print('whos that sexy lady????')
        # print('you are!!!!')

def test_multiply_by():
    emptylist = []
    result = multiply_by(emptylist, 2)
    print_test('test_multiply_by emptylist and 2', emptylist == [])
    print_test('test_multiply_by emptylist and 2', result == [])

    list1 = [6]
    result = multiply_by(list1, 4)
    print_test('test_multiply_by list1 and 4', list1 == [6])
    print_test('test_multiply_by list1 and 4', result == [24])

    list2 = [8]
    result = multiply_by(list2, 4)
    print_test('test_multiply_by list2 and 4', list2 == [8])
    print_test('test_multiply_by list2 and 4', result == [32])

    list3 = [1,2,3]
    result = multiply_by(list3, 4)
    print_test('test_multiply_by list3 and 4', list3 == [1,2,3])
    print_test('test_multiply_by list3 and 4', result == [4,8,12])

    list4 = [3,5,7]
    result = multiply_by(list4, 3)
    print_test('test_multiply_by list4 and 3', list4 == [3,5,7])
    print_test('test_multiply_by list4 and 3', result == [9,15,21])


''' Purpose:
        creates a new list of all values from numbers
        mutiplied by multiplier
    Args:
        numbers (list): the list of numbers
        multiplier (int): the number to mutiply by
    Returns:
        (list): the new list
    '''
# TODO: define multiply_by here...
def multiply_by(numbers, multiplier):
    new_list = []
    for num in numbers:
        num = num * multiplier
        new_list.append(num)

    return new_list



def test_get_above():
    emptylist = []

    result = get_above(emptylist, 0)
    print_test('test_multiply_by emptylist 0', emptylist == [])
    print_test('test_multiply_by emptylist 0', result == [])

    list4 = [1, 4, 7, 5]
    result = get_above(list4, 0)
    print_test('test_get_above all above 0', list4 == [1, 4, 7, 5])
    print_test('test_get_above all above 0', result == [1, 4, 7, 5])

    list5 = [4, 5, 6, 7]
    result = get_above(list5, 3)
    print_test('test_get_above all above 3', list5 == [4, 5, 6, 7])
    print_test('test_get_above all above 3', result == [4, 5, 6, 7])

    list6 = [9, 10, 11, 12]
    result = get_above(list6, 10)
    print_test('test_get_above all above 10', list6 == [9, 10, 11, 12])
    print_test('test_get_above all above 10', result == [11,12])

    list7 = [20, 30, 15, 50]
    result = get_above(list7, 25)
    print_test('test_get_above all above 25', list7 == [20, 30, 15, 50])
    print_test('test_get_above all above 25', result == [30, 50])


''' Purpose:
        creates a new list and copies only values from numbers
        to the new list that are bigger than the threshold n
    Args:
        numbers (list): the list of numbers
        n (int): the threshold to indicate which values to keep
    Returns:
        (list): the new list
    '''
# TODO: define get_above here...
def get_above(list, threshold):
    new_list = []
    for val in list:
        if (val > threshold):
            new_list.append(val)

    return new_list






def test_sum_odd():
    emptylist = []
    result = sum_odd(emptylist)
    print_test('test_sum_odd emptylist', emptylist == [])
    print_test('test_sum_odd emptylist', result==0)

    list1even = [6]
    result = sum_odd(list1even)
    print_test('test_sum_odd list1even', list1even == [6])
    print_test('test_sum_odd list1even', result==0)

    list2even = [8]
    result = sum_odd(list2even)
    print_test('test_sum_odd list2even', list2even == [8])
    print_test('test_sum_odd list2even', result==0)

    list3 = [1,2,3,4]
    result = sum_odd(list3)
    print_test('test_sum_odd list3', list3 == [1,2,3,4])
    print_test('test_sum_odd list3', result==4)

    list4 = [3,5,6,8]
    result = sum_odd(list4)
    print_test('test_sum_odd list4', list4 == [3,5,6,8])
    print_test('test_sum_odd list4', result==8)

''' Purpose:
        calculates the sum of the odd values in numbers
    Args:
        numbers (list): the list of integers
    Returns:
        (int): the sum
    '''
# TODO: define sum_odd here...
def sum_odd(list):
    sum = 0
    for num in list:
        if (num%2==1):
            sum = sum + num

    return sum






def test_get_min():
    increasing = [1, 3, 4, 5]
    result = get_min(increasing)
    print_test('test_get_min increasing list', increasing == [1, 3, 4, 5])
    print_test('test_get_min increasing list', result == 1)

    increasing2 = [2, 3, 4, 5]
    result = get_min(increasing2)
    print_test('test_get_min increasing2 list', increasing2 == [2, 3, 4, 5])
    print_test('test_get_min increasing2 list', result == 2)

    my_list = [10,12,14,15]
    result = get_min(my_list)
    print_test('test_get_min my_list list', my_list == [10,12,14,15])
    print_test('test_get_min my_list list', result == 10)

    my_new_list = [17,94,4,6]
    result = get_min(my_new_list)
    print_test('test_get_min my_new_list list', my_new_list == [17,94,4,6])
    print_test('test_get_min my_new_list list', result == 4)


''' Purpose:
        finds the smallest value in numbers
    Args:
        numbers (list): the list of integers
    Precondition:
        numbers is not empty
    Returns:
        (int): the smallest value
    '''
# TODO: define get_min here...
def get_min(list):
    min = list[0]
    for num in list:
        if (num < min):
            min = num
    return min





def test_contain_negative():
    emptylist = []
    result = contain_negative(emptylist)
    print_test('test_contain_negative emptylist - false', emptylist == [])
    print_test('test_contain_negative emptylist - false', not(result))

    list_no_negs1 = [1, 2, 16, 8, 3]
    result = contain_negative(list_no_negs1)
    print_test('test_contain_negative list_no_negs1 - false', list_no_negs1 == [1, 2, 16, 8, 3])
    print_test('test_contain_negative list_no_negs1 - false', not(result))

    list_all_negs2 = [-1, -2, -16, -8]
    result = contain_negative(list_all_negs2)
    print_test('test_contain_negative list_all_negs2 - true', list_all_negs2 == [-1, -2, -16, -8])
    print_test('test_contain_negative list_all_negs2 - true', result)

    list_all_negs3 = [-5, -2, 16, 8]
    result = contain_negative(list_all_negs3)
    print_test('test_contain_negative list_all_negs3 - true', list_all_negs3 == [-5, -2, 16, 8])
    print_test('test_contain_negative list_all_negs3 - true', (result))


''' Purpose:
        determine whether numbers contains any negative values
    Args:
        numbers (list): the list of integers
    Returns:
        (bool): true if contains any negatives, false otherwise
    '''
# TODO: define contains_negative here...
def contain_negative(list):
    for num in list:
        if (num>=0):
            result = False
            return result
        else:
            result = True
            return result






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
