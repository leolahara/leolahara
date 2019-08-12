# assignment1.py
#
# Student name:Leola Hara
# Student id:  V00923578






def main():
    print("Welcome")
    # print()
    # You will call your functions here to test them:
    print_logo()
    calc_surface_area()

# DEFINE your functions after this line:
#purpose is to print a pig
def print_pig():
    print('  ^  ^')
    print('   --')
    print(' (O  O)')
    print('  (oo)')
    print('@(")_(")')

#purpose is to print a frog
def print_frog():
    print('  @..@')
    print('  ----')
    print('( >__< )')
    print('""    ""')

#purpose is to print a logo between each asci animal
def print_logo():
    print('/~~~~~~\\')
    print_frog()
    print('/~~~~~~\\')
    print_pig()
    print('/~~~~~~\\')
    print_frog()
    print('/~~~~~~\\')
    print_pig()
    print('/~~~~~~\\')
    print('/~~~~~~\\')

#purpose is to calculate surface area of a cylinder with height 6m and diameter 5m
def calc_surface_area():
    height = 6
    diameter = 5
    pi = 3.14
    radius = diameter / 2.0
    circumference = pi * diameter
    circle_area = pi * radius*radius
    wall_area = circumference * height
    print(str(circle_area*2 + wall_area) + " square meters" )

# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
