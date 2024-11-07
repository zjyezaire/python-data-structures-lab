# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()



# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ['Zaire', 'Josiah', 'Yancy']
    second_student = students[1]
    last_student = students[-1]
    return students
# Call the function and print the result
print("\n")
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ['fried chicken, ', 'mac and cheese, ', 'yams' ]
    meal = ''

    for food in foods:
        meal += food
    return meal

    

# Call the function and print the result
print('Exercise 2:', combine_foods())




# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    foods = ('oxtail,', 'rice n peas, ', 'cabbage')
    last_two_foods = foods[-2]
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())



# Exercise 4: Dictionaries and String Formatting

# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: 
# “I was born in <city>, <state> - population of <population>”

def hometown_info():
    home_town = {
        'city': 'Peekskill',
        'state': 'New York',
        'population': '25,442'
    }
    
    # Assign formatted string to home_town_message
    home_town_message = (f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.")

    # Return the message
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())

