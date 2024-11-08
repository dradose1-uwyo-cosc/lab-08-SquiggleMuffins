# Jacquelyn Hall
# UWYO COSC 1010
# Submission Date 11/6/2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

num = input("Please put interger or float here to convert: ")

def con(num):
    if num[1:].isdigit(): 
        return int(num)
    elif num[0] == '-':
        return int(num)

    if num.count('.') == 1:
        le, ri = num.split('.')
        
        if (le.isdigit() or (le[0] == '-' and le[1:].isdigit())) and ri.isdigit():
            return float(num)
        
    return False
    
print(con(f"{num}"))
    

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def si(m, b, low, up):

    try:
        low = int(low)
        up = int(up)
        if low > up:
            return False
    except ValueError:
        return False
    
    yv = [(m * x) + b for x in range(low, up)]
    return yv

while True:
    
    mim = input("Please type slope here or 'exit' to quit!: ")
    if mim.lower() == "exit":
        break
    bim = input("Please enter y-intercept or 'exit' to quit!:")
    if bim.lower() == "exit":
        break
    lim = input("Please enter lower bound or 'exit' to quit!:")
    if lim.lower() == "exit":
        break
    uim = input("Please enter upper bound or 'exit' to quit!:")
    if uim.lower() == "exit":
        break

    m = float(mim)
    b = float(bim)

    res = si(m, b, lim, uim)
    
    if res is not False:
        print(f"The y values are:{res}")
    else:
     print("Please type in valid bounds")

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

mix = 0

def root(num):
    if num > 0:
        return num**.5
    else:
        return False
    
def quad(a, b, c):
    mix = root(b**2 - (4 * a * c))

    if mix > 0:
        print(f"{(-b + mix)/(2 * a)}")
        print(f"{(-b - mix)/(2 * a)}")

while True:

    a = input("Please type in a value or type 'exit to quit:")
    if a.lower == "exit":
        break

    b = input("Please type in b value:")
    c = input("Please type in c value:")

 