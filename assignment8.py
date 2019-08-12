# assignment8.py
#
# Student name: Leola Hara
# Netlink id:  V00923578

THRESHOLD = 0.1 # to be used to compare floating point values

# position of specified data in a row of the input data file
NAME_INFILE    = 1
TEAM_INFILE    = 2
POS_INFILE     = 3
PPG_INFILE     = 18
RPG_INFILE     = 19
SPG_INFILE     = 23
BPG_INFILE     = 24

# position of specified data within a tuple
NAME_TUPLE  = 0
TEAM_TUPLE  = 1
POS_TUPLE   = 2
PPG_TUPLE   = 3
RPG_TUPLE   = 4
SPG_TUPLE   = 5
BPG_TUPLE   = 6

passed = 0
tests = 0

''' Complete this assignment by doing the following for each function:
    - uncommenting one test function call in main
    NOTE: each test function has at least one test,
    but you should add additional tests where you feel necessary

    - implement the function (write the documentation and define the function)
    NOTE: follow the documentation provided here for implementing each function

    - repeat until all functions are tested and implemented
    '''
def main():
    print('Assignment 8')
    test_read_file()
    test_get_val()
    test_filter_list()
    test_contains()
    test_get_unique()
    test_get_max()
    test_get_avg()
    test_get_report()
    print(passed, '/', tests, ' tests passed')

def test_read_file():
    result = read_file('notthere.csv')
    print_test('test_filename', result == None)

    result = read_file('4line.csv')
    expected = [('Will Barton', 'Den', 'G', 9.1, 4.8, 0.29, 0.64),
                ('Malik Beasley', 'Den', 'G', 8.1, 3.4, 0.21, 0.07),
                ('Marc Gasol', 'Tor', 'C', 8.4, 6, 1.15, 1.08),
                ('Torrey Craig', 'Den', 'F', 6.6, 5.1, 0.5, 0.36)]
    print(result)
    print_test('test_filename', expected == result)

''' Purpose:
        opens filename for reading and
        creates a tuple for each line with:
          name, team, position, PPG, SPG, RPG and BPG into data
        where name, team and position are stored as Strings and
          PPG, SPG, RPG and BPG are stored as floats
        appends tuple to data
    Args:
        filename(str): the name of a file with raw stats
    Precondition:
        file is in expected format
    Returns:
        (list of tuples): data
        '''
#TODO: define read_file
def read_file(filename):
    data = []
    try:
        file_handle = open(filename, 'r')

        index = 1
        for line in file_handle:

            if index!=1:
                new_list = line.split(',')
                tuple = (new_list[NAME_INFILE],new_list[TEAM_INFILE],new_list[POS_INFILE],float(new_list[PPG_INFILE]),float(new_list[RPG_INFILE]),float(new_list[SPG_INFILE]),float(new_list[BPG_INFILE]))
                data.append(tuple)
            index += 1

        return data
    except FileNotFoundError:
        print('cant find the file')






def test_get_val():
    empty = []
    list3 = [('Will Barton', 'Den', 'G', 9.1, 4.8, 0.29, 0.64),
             ('Malik Beasley', 'Den', 'G', 8.1, 3.4, 0.21, 0.07),
             ('Marc Gasol', 'Tor', 'C', 8.4, 6, 1.15, 1.08),
             ('Torrey Craig', 'Den', 'F', 6.6, 5.1, 0.5, 0.36)]

    result = get_val(empty, 0)
    print_test('test_get_stat', result == [])

    result = get_val(list3, 0)
    print_test('test_get_stat',
               result == ['Will Barton', 'Malik Beasley', 'Marc Gasol', 'Torrey Craig'])

    result = get_val(list3, 4)
    print_test('test_get_stat', result == [4.8, 3.4, 6, 5.1])

''' Purpose:
        extracts value from each tuple at specified index in tuple
        creates a newlist of those values
    Args:
        data(list): list containing tuples with:
            name, team, position, PPG, SPG, RPG and BPG into data
        index(int): the position of tuple to extract
    Precondition:
        tuples are in expected format
    Returns:
        (list): newlist
    '''
#TODO: define get_val...
def get_val(data, index):
    new_list = []
    for tuple in data:
        val = tuple[index]
        new_list.append(val)

    return new_list






def test_filter_list():
    empty = []
    list3 = [('Will Barton', 'Den', 'G', 9.1, 4.8, 0.29, 0.64),
             ('Malik Beasley', 'Den', 'G', 8.1, 3.4, 0.21, 0.07),
             ('Marc Gasol', 'Tor', 'C', 8.4, 6, 1.15, 1.08),
             ('Torrey Craig', 'Den', 'F', 6.6, 5.1, 0.5, 0.36)]

    result = filter_list(empty, 0, 'x')
    print_test('test_filter_list', result == [])

    result = filter_list(list3, 1, 'Den')
    print_test('test_filter_list',
               result == [('Will Barton', 'Den', 'G', 9.1, 4.8, 0.29, 0.64),
                          ('Malik Beasley', 'Den', 'G', 8.1, 3.4, 0.21, 0.07),
                          ('Torrey Craig', 'Den', 'F', 6.6, 5.1, 0.5, 0.36)])

    result = filter_list(list3, 1, 'Tor')
    print_test('test_filter_list',
               result == [('Marc Gasol', 'Tor', 'C', 8.4, 6, 1.15, 1.08)])

    result = filter_list(list3, 2, 'G')
    print_test('test_filter_list',
    result == [('Will Barton', 'Den', 'G', 9.1, 4.8, 0.29, 0.64),
               ('Malik Beasley', 'Den', 'G', 8.1, 3.4, 0.21, 0.07)])

''' Purpose:
        creates a newlist of tuples of only those tuples in data which
        have the specified keep value at the specified index in the tuple
    Args:
        data(list): list containing tuples with:
         name, team, position, PPG, SPG, RPG and BPG into data
        index(int): the position of tuple to filter on
        keep(str or int): the value to filter on
    Precondition:
        tuples are in expected format
    Returns:
        (list of tuples): newlist
    '''
#TODO: define filter_list...
def filter_list(data, index, keep):
    new_list = []
    for tuple in data:
        if (tuple[index] == keep):
            new_list.append(tuple)
    return new_list








def test_contains():
    empty = []
    result = contains(empty, 4)
    print_test('test_contains', result == False)
    print_test('test_contains', empty == [])

    list_unique = [3,4,6,7]
    result = contains(list_unique,8)
    print_test('test_contains', result == False)

    result = contains(list_unique,6)
    print_test('test_contains', result == True)

''' Purpose:
        determines whether elem is contained in data
    Args:
        data(list): list with elements of the same type as elem
        elem(str or float): value looking for in data
    Precondition:
        element in data and elem are the same type
    Returns:
        (bool): True if elem is found, False otherwise
    '''
#TODO: define contains...
def contains(data, elem):
    for tuple in data:
        if tuple == elem:
            return True

    return False








def test_get_unique():
    empty = []
    result = get_unique(empty)
    print_test('test_get_unique', result == [])
    print_test('test_get_unique', empty == [])

    list_unique = [3,4,6,7]
    result = get_unique(list_unique)
    print_test('test_get_unique', result == [3,4,6,7])
    print_test('test_get_unique', list_unique == [3,4,6,7])

    list_same = [3,3,3]
    result = get_unique(list_same)
    print_test('test_get_unique', result == [3])
    print_test('test_get_unique', list_same == [3,3,3])

    list_3 = [3,2,1,2,3,3,1,2]
    result = get_unique(list_3)
    print_test('test_get_unique',
               len(result) == 3 and contains(result, 1) and
               contains(result, 2) and contains(result, 3))
    print_test('test_get_unique', list_3 == [3,2,1,2,3,3,1,2])

''' Purpose:
        creates a newlist of elements from data without duplicates
    Args:
        data(list): list of elements
    Returns:
        (list): the newlist
    '''
#TODO: define get_unique...
def get_unique(data):
    new_list = []

    for num in data:
        if contains(new_list, num) == False:
            new_list.append(num)

    return new_list










def test_get_max():
    list4 = [('Will Barton',   'Den', 'G', 9.1, 4.8, 0.29, 0.64),
             ('Malik Beasley', 'Den', 'G', 8.1, 6.4, 0.21, 0.07),
             ('Torrey Craig',  'Den', 'F', 6.6, 5.1, 0.5,  0.36),
             ('Marc Gasol',    'Tor', 'C', 8.4, 6,   1.15, 1.08)]
    result = get_max(list4, 3)
    print_test('test_get_max', result == ('Will Barton', 'Den', 'G', 9.1, 4.8, 0.29, 0.64))
    print_test('test_get_max', list4 == [('Will Barton', 'Den', 'G', 9.1, 4.8, 0.29, 0.64),
                                         ('Malik Beasley', 'Den', 'G', 8.1, 6.4, 0.21, 0.07),
                                         ('Torrey Craig', 'Den', 'F', 6.6, 5.1, 0.5, 0.36),
                                         ('Marc Gasol', 'Tor', 'C', 8.4, 6, 1.15, 1.08)])

    result = get_max(list4, 4)
    print_test('test_get_max', result == ('Malik Beasley', 'Den', 'G', 8.1, 6.4, 0.21, 0.07))
    result = get_max(list4, 6)
    print_test('test_get_max', result == ('Marc Gasol', 'Tor', 'C', 8.4, 6, 1.15, 1.08))

''' Purpose:
        finds the tuple with the max value at specified search_index in tuple
    Args:
        data(list): list containing tuples with:
         name, team, position, PPG, SPG, RPG and BPG into data
         search_index(int): index in tuple being considered
    Precondition:
        data is not empty
    Returns:
        (tuple): the tuple with max value
    '''
#TODO: define get_max...
def get_max(data, search_index):

    max = data[0]
    for tuple in data:
        if tuple[search_index]>max[search_index]:
            max = tuple
    return max






def test_get_avg():
    empty =[]
    result = get_avg(empty)
    print_test('test_get_avg', result == 0)

    list4 = [9.1, 4.8, 0.29, 0.64]
    result = get_avg(list4)
    expected = (9.1 + 4.8 + 0.29 + 0.64)/4
    print_test('test_get_avg', abs(expected-result)<THRESHOLD)

''' Purpose:
        calculates the average of the values in data
        average is 0 if data is empty
    Args:
        data(list): list containing numbers
    Returns:
        (float): average
    '''
#TODO: define get_avg
def get_avg(data):
    try:
        sum = 0
        length_of_data = len(data)
        for num in data:
            sum = sum + num

        average = sum / length_of_data
        return average

    except ZeroDivisionError:
        return 0








def test_get_report():
    get_report('4line.csv','4lineout.csv')
    get_report('2018.csv','2018out.csv')
    get_report('2017.csv','2017out.csv')

''' Purpose:
        gets a report of stats from filein and writes results to fileout
    Args:
        filein(str): name of file to read from
        fileout(str): name of file to write to
    Precondition:
        filein refers to a file in expected format
    '''
def get_report(filein, fileout):


    # if you are unsure what the following is doing
    #  read the documentation for the functions being called
    #  and uncomment the print statements below...

    data = read_file(filein)
    # print('data after read_file:\n', data)
    teams = get_val(data, 1)
    # print('teams after get_val:\n', teams)
    teams = get_unique(teams)
    # print('teams after get_unique:\n', teams)
    write_stats(data, teams, fileout)


''' Purpose:
        gets a report of stats from filein and writes results to fileout
        - a header row that specifies the title of each column separated by commas,
        followed a row for each team with the following values separated by commas:
        - the team name, the average PPG, SPG, RPG and BPG for each team
        - the name of the highest scoring forward followed by that player's stats:
          - PPG, SPG, RPG and BPG
    Args:
        data(list): list containing tuples with:
            name, team, position, PPG, SPG, RPG and BPG into data
        rows(list): list with unique teams in data
        fileout(str): name of file to write to
    Precondition:
        data is in expected format, rows has no duplicates
    '''
#TODO: define write_stats...
# HINT: you will need to make use of some of the functions you have already written
def write_stats(data, rows, file_out):

    output_file = open(file_out, 'w')
    output_file.write('Team,Average Points/Game,Average Rebounds/Game,Average Steals/Game,Average Blocks/Game\n')

    for team in rows:
        filtered_team = filter_list(data, TEAM_TUPLE, team)

        ppg = get_val(filtered_team, PPG_TUPLE)
        average_ppg = get_avg(ppg)
        rpg = get_val(filtered_team, RPG_TUPLE)
        average_rpg = get_avg(rpg)
        spg = get_val(filtered_team, SPG_TUPLE)
        average_spg = get_avg(spg)
        bpg = get_val(filtered_team, BPG_TUPLE)
        average_bpg = get_avg(bpg)

        new_stats = [team, "{:.1f}".format(average_ppg), "{:.1f}".format(average_rpg), "{:.1f}".format(average_spg), "{:.1f}".format(average_bpg)]

        for i in range(len(new_stats)):
            output_file.write(new_stats[i])
            if i != (len(new_stats)-1):
                output_file.write(",")

        output_file.write("\n")

    forward = filter_list(data, POS_TUPLE, 'F') + filter_list(data, POS_TUPLE, 'SF')
    best_forward = get_max(forward, PPG_TUPLE)
    best_forward_name = best_forward[NAME_TUPLE]
    best_forward_ppg = best_forward[PPG_TUPLE]
    best_forward_rpg = best_forward[RPG_TUPLE]
    best_forward_spg = best_forward[SPG_TUPLE]
    best_forward_bpg = best_forward[BPG_TUPLE]


    output_file.write("highest scoring forward is:,")
    output_file.write(best_forward_name)
    output_file.write('\n')
    output_file.write("points per game:, ")
    output_file.write(str(best_forward_ppg))
    output_file.write('\n')
    output_file.write("rebounds per game:,")
    output_file.write(str(best_forward_rpg))
    output_file.write('\n')
    output_file.write("steals per game:,")
    output_file.write(str(best_forward_spg))
    output_file.write('\n')
    output_file.write("blocks per game:,")
    output_file.write(str(best_forward_bpg))
    output_file.write('\n')

    output_file.close()









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
