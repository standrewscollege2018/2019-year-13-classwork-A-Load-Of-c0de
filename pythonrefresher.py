# print() is a function
print("Hello world")
print(25)

# variables don't have a dollar sign!
# when naming we use snake_case, so no uppercase letter or symbols other than under underscore
first_name = "John"
last_name = "Smith"

# we can print variables or even text and variables
print(first_name)
print("Hello", first_name)
# using format() is a more elegant way of combining text and variables
print("Hello {} {}".format(first_name, last_name))


# To get user input we use rhe input() function. Input should be assigned to a variable.
city_of_birth = input("Where were you born {}?".format(first_name))


print("Wow! I too was born in {}!".format(city_of_birth))

# when we are expecting non-string input, we "cast" our input as a specific data type
year_of_birth = int(input("What year were you born in?"))

age = 2019 - year_of_birth
print("That makes you appriximately {} years old".format(age))

# Lists are a way of storing more than one piece of data
my_list = ["Bananas", 25, True, "Golf"]
# the index of an item reers to its location in the list. It starts at zero (0). 
# when retrieving data from a list we pull it out by its index
print(my_list[0])
# lists are mutable, meaning we can edit them after they are set
# to add data to a list, we use either insert() or append()
my_list.append("Table")
print(my_list)
my_list.insert(1, "Rinay")
# go update a list item, just overwrite it
my_list[1] = "Shannon"
print(my_list)

# to delete from a list

del my_list[4]
print(my_list)

add = input("What is your name?")
my_list.append(add)
print(my_list)

