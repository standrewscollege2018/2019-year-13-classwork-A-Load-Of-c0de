def is_even(check_number):
    """ This function calculates wheter a number is even, returning True or False """
    """ Define all functions at the top of the program """
    
    if check_number % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_even(number)==True:
    print("Even")
else:
    print("Odd")