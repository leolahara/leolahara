# assignment9.py
#
# Student name: Leola Hara
# Netlink id:  V00923578

passed = 0
tests = 0


''' Complete this assignment by doing the following for each function:
    - uncommenting one test function call in main
    NOTE: each test function tests one of the functions you must write
          ensure your implementation will work for other inputs
                 as we will test with other inputs
          all inputs we test with are guaranteed to be in the specifed format

    - implement the function (define the function)
    NOTE: follow the documentation provided here for implementing each function

    - repeat until all functions are tested and implemented
    '''


def main():
    print('Assignment 9')
    test_read_file()
    test_require_at_most_1()
    test_max_value_length()
    test_get_with_max_value_length()
    test_invert_dictionary()
    test_most_used()
    print(passed, '/', tests, ' tests passed')

def test_read_file():
    result = read_file('notthere.csv')
    print_test('test_read_file' , result == None)

    result = read_file('cscprereqs_1.csv')
    expected = {'CSC 110': ['MATH 12'],'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 116': ['CSC 110', 'CSC 111']}
    print_test('test_read_file' , result == expected)

    result = read_file('cscprereqs.csv')
    expected = {'CSC 100': [],'CSC 103': [], 'CSC 105': [], 'CSC 106': [], 'CSC 110': ['MATH 12'], 'CSC 111': ['MATH 12'], 'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 116': ['CSC 110', 'CSC 111'], 'CSC 205': ['MATH 151', 'MATH 211', 'SENG 265'], 'CSC 225': ['CSC 115', 'CSC 116', 'MATH 122'], 'CSC 226': ['CSC 225'], 'CSC 230': ['CSC 115', 'CSC 116'], 'CSC 299': ['CSC 115', 'CSC 226', 'CSC 230', 'SENG 265'], 'CSC 305': ['CSC 226', 'MATH 110', 'MATH 211', 'SENG 265'], 'CSC 320': ['CSC 226'], 'CSC 322': ['CSC 115', 'CSC 116', 'MATH 122', 'PHIL 203'], 'CSC 330': ['CENG255', 'CSC 226', 'CSC 230', 'CSC 320', 'CSC 360', 'ECE 255', 'SENG 265'], 'CSC 349A': ['CSC 110', 'CSC 111', 'MATH 110', 'MATH 200', 'MATH 201', 'MATH 202', 'MATH 211'], 'CSC 350': ['CSC 225', 'CSC 230'], 'CSC 355': ['CENG 255', 'CSC 230', 'ECE 255', 'MATH 122'], 'CSC 360': ['CENG 255', 'CSC 230', 'ECE 255', 'SENG 265'], 'CSC 361': ['CENG 255', 'CSC 226', 'CSC 230', 'ECE 255', 'SENG 265'], 'CSC 370': ['CSC 226', 'SENG 265'], 'CSC 371': ['MATH 100', 'MATH 102', 'MATH 120'], 'CSC 375': ['HINF 130', 'HINF 140', 'SENG 265']}
    print_test('test_read_file' , result == expected)

''' Purpose:
        Creates a new dictionary and
        reads filename creating a dictionary entry
        for each row in the file
        The first element in the row is the key,
        the remaining elements(>=0) are put in a sorted list
        and stored as the value to that key
    Args:
        filename (str): name of the file to read from
    Returns:
        (dictionary): the new dictionary in the form
            course name as the key (str), and a list of that course's
            prerequisites as the value  (list of str)
        None if IOError on opening filename
    '''
# TODO: define read_file here...
# You may use Python built-in sort function
def read_file(filename):
    try:

        dict = {}
        file_handle = open(filename)

        for line in file_handle:
            line = line.strip("\n")
            line = line.split(",")
            courses = line[0]
            prerequisites = line[1:]
            prerequisites.sort()
            dict[courses] = prerequisites

        file_handle.close()
        return dict

    except FileNotFoundError:
        return







def test_require_at_most_1():
    empty = {}
    result = require_at_most_1(empty)
    print_test('test_require_at_most_1', result == [])

    data = {'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 106': [], 'CSC 116': ['CSC 110', 'CSC 111']}
    result = require_at_most_1(data)
    print_test('test_require_at_most_1', result == ['CSC 106', 'CSC 111'])

    big_data = read_file('cscprereqs.csv')
    result = require_at_most_1(big_data)
    print_test('test_require_at_most_1', result == ['CSC 100','CSC 103','CSC 105','CSC 106','CSC 110','CSC 111','CSC 226','CSC 320'])

''' Purpose:
        Creates a new list of course names from data
        that have 1 or less prerequisites
    Args:
        data (dictionary): a dictionary in the form
            course name as the key (str), and a list of that course's
            prerequisites as the value  (list of str)
    Returns:
        (list): the new list of course names
    '''
# TODO: define test_require_at_most_1 here...
# You may use Python built-in sort function
def require_at_most_1(data):
    list = []

    for courses in data:
        if len(data[courses]) <=1:
            list.append(courses)
    list.sort()
    return list





def test_max_value_length():
    empty = {}
    result = max_value_length(empty)
    print_test('test_max_value_length', result == 0)

    data0 = {'CSC 111': [],'CSC 115': [], 'CSC 106': []}
    result = max_value_length(data0)
    print_test('test_max_value_length', result == 0)

    data2 = {'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 106': [], 'CSC 116': ['CSC 110', 'CSC 111']}
    result = max_value_length(data2)
    print_test('test_max_value_length', result == 2)

    big_data = read_file('cscprereqs.csv')
    result = max_value_length(big_data)
    print_test('test_max_value_length', result == 7)

''' Purpose:
        returns the max length of the value list in data
    Args:
        data (dictionary): a dictionary in the form
            (str) as the key, and a (list of str) as the value
    Returns:
        (int): max length, 0 if data is empty
    '''
# TODO: define max_value_length here...
def max_value_length(data):
    max_needed = 0
    for courses in data:
        if len(data[courses])>max_needed:
            max_needed = len(data[courses])
    return max_needed




def test_get_with_max_value_length():
    data0 = {'CSC 111': [],'CSC 115': [], 'CSC 106': []}
    result = get_with_max_value_length(data0)
    print_test('test_get_with_max_value_length', result == ['CSC 106', 'CSC 111', 'CSC 115'])

    data2 = {'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 106': [], 'CSC 116': ['CSC 110', 'CSC 111']}
    result = get_with_max_value_length(data2)
    print_test('test_get_with_max_value_length', result == ['CSC 115', 'CSC 116'])

    big_data = read_file('cscprereqs.csv')
    result = get_with_max_value_length(big_data)
    print_test('test_get_with_max_value_length', result == ['CSC 330', 'CSC 349A'])

''' Purpose:
        creates a new list of names of only those courses (keys) that have
        a value with the longest length (value - list of str)
        and puts this list in sorted order
    Args:
        data (dictionary): a dictionary in the form
            (str) as the key, and a (list of str) as the value
    Returns:
        (list): the new list sorted
    '''
# TODO: define get_with_max_value_length here...
# You may use Python built-in sort function
def get_with_max_value_length(data):
    list_of_courses = []
    max_value = 0

    for course in data:
        if len(data[course])>max_value:
            max_value = len(data[course])

    for course in data:
        if len(data[course])== max_value:
            list_of_courses.append(course)

    list_of_courses.sort()
    return list_of_courses










def test_invert_dictionary():
    empty = {}
    result = invert_dictionary(empty)
    print_test('test_invert_dictionary', result == {})

    data0 = {'CSC 111': [],'CSC 115': [], 'CSC 106': []}
    result = invert_dictionary(data0)
    print_test('test_invert_dictionary', result == {})


    data2 = {'CSC 111': ['MATH 12'], 'CSC 116': ['CSC 110', 'CSC 111'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 106': []}
    result = invert_dictionary(data2)
    expected = {'MATH 12': [ 'CSC 111'],
                'CSC 110': [ 'CSC 115', 'CSC 116'],
                'CSC 111': [ 'CSC 115', 'CSC 116']}
    print_test('test_invert_dictionary', result == expected)

    big_data = read_file('cscprereqs.csv')
    result = invert_dictionary(big_data)
    expected = {'MATH 12': ['CSC 110', 'CSC 111'], 'CSC 110': ['CSC 115', 'CSC 116', 'CSC 349A'], 'CSC 111': ['CSC 115', 'CSC 116', 'CSC 349A'], 'MATH 151': ['CSC 205'], 'MATH 211': ['CSC 205', 'CSC 305', 'CSC 349A'], 'SENG 265': ['CSC 205', 'CSC 299', 'CSC 305', 'CSC 330', 'CSC 360', 'CSC 361', 'CSC 370', 'CSC 375'], 'CSC 115': ['CSC 225', 'CSC 230', 'CSC 299', 'CSC 322'], 'CSC 116': ['CSC 225', 'CSC 230', 'CSC 322'], 'MATH 122': ['CSC 225', 'CSC 322', 'CSC 355'], 'CSC 225': ['CSC 226', 'CSC 350'], 'CSC 226': ['CSC 299', 'CSC 305', 'CSC 320', 'CSC 330', 'CSC 361', 'CSC 370'], 'CSC 230': ['CSC 299', 'CSC 330', 'CSC 350', 'CSC 355', 'CSC 360', 'CSC 361'], 'MATH 110': ['CSC 305', 'CSC 349A'], 'PHIL 203': ['CSC 322'], 'CENG255': ['CSC 330'], 'CSC 320': ['CSC 330'], 'CSC 360': ['CSC 330'], 'ECE 255': ['CSC 330', 'CSC 355', 'CSC 360', 'CSC 361'], 'MATH 200': ['CSC 349A'], 'MATH 201': ['CSC 349A'], 'MATH 202': ['CSC 349A'], 'CENG 255': ['CSC 355', 'CSC 360', 'CSC 361'], 'MATH 100': ['CSC 371'], 'MATH 102': ['CSC 371'], 'MATH 120': ['CSC 371'], 'HINF 130': ['CSC 375'], 'HINF 140': ['CSC 375']}
    print_test('test_invert_dictionary', result == expected)

''' Purpose:
        Creates a new dictionary from the given dictionary data where,
        each of the prerequisite course names in the lists of values
            becomes a key in the new dictionary
            and the value for each key (prerequisite course) in the new dictionary is
            a list of the courses that require that key (prerequisite course) in sorted order
    Args:
        data (dictionary): a dictionary in the form
            the course (str) as the key,
            and the prerequisites to that course (list of str) as the value
    Returns:
        (dictionary): the new dictionary in the form
            the prequisite course (str) as the key,
            and the courses that require that prerequisite course (list of str) as the value

    '''
# TODO: define invert_dictionary here...
# You may use Python built-in sort function
def invert_dictionary(data):
    inverted_dict = {}
    my_list = []

    for course in data:
        for prequisite in data[course]:
            inverted_dict[prequisite] = []

    for course in data:
        for prequisite in data[course]:
            inverted_dict[prequisite].append(course)

    for prequisite in inverted_dict:
        inverted_dict[prequisite].sort()


    return inverted_dict







def test_most_used():
    empty = {}
    result = most_used(empty)
    print_test('test_most_used', result == [])

    data0 = {'CSC 111': [],'CSC 115': [], 'CSC 106': []}
    result = most_used(data0)
    print_test('test_most_used', result == [])

    data2 = {'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 106': [], 'CSC 116': ['CSC 111']}
    result = most_used(data2)
    print_test('test_most_used', result == ['CSC 111'])

    data3 = {'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'],
            'CSC 106': [], 'CSC 116': ['CSC 110', 'CSC 111'], 'CSC 110': ['MATH 12'],}
    result = most_used(data3)
    print_test('test_most_used', result == ['CSC 110', 'CSC 111', 'MATH 12'])

    big_data = read_file('cscprereqs.csv')
    result = most_used(big_data)
    expected = ['SENG 265']
    print_test('test_most_used', result == expected)

''' Purpose:
        creates a new list of only the course names which are the
        most frequently used a prerequisites from data
    Args:
        data (dictionary): a dictionary in the form
            the course (str) as the key,
            and the prerequisites to that course (list of str) as the value
    Returns:
        (list): the new list of most frequently used course names
    '''
def most_used(data):
    used = invert_dictionary(data)
    most_used = get_with_max_value_length(used)
    return most_used




''' Purpose:
        prints test_name followed by ': passed' if expression evaluates to True,
        prints test_name followed by ': failed' if expression evaluates to False
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
