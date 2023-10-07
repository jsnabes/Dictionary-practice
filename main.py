# Creating dictonaries to store student data
database1 = {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"}
database2 = {"name": "Klaus", "hometown": "Frankfurt","favorite_food": "pizza"}
database3 = {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
all_students = database1 | database2 | database3

# First function
def list_names(all_students):
    names = list(all_students)
    print(names)
list_names = ('x', 'y', 'z')

# Start of second function
def prompt_for_action():
    while True:
        #prompting user to add, view or quit
        action_request = input("Please select which action you'd like to do:"
                               "add, view or quit ")
        # return nothing and quit if user wants to quit
        if action_request in ['Q', 'q']:
            return None
# Defining function to obtain student number, if user selected 'view'
def view_student(options):
    student_choice = input(f"{list_names}"
                        f"Which student would you like to learn more about?"
                        f"Enter a number 1-3: ")
# Printing "Student "#" is "NAME"
def print_student_details(student_number):
        print(f"Student {student_number} is {list_names[(student_number)]}. What would you like to know? ")

def prompt_for_category():
    while True:
        category_response = input("Enter: H for 'hometown' or F for 'favorite food: ")
    if category_response not in ['H', 'F']:
        print("That category does not exist. Please try again. Enter 'hometown' or 'favorite food': ")
    else:
      return category_response

# Printing "STUDENT is from HOMETOWN". Should reference back to dict.
def print_category_details(cateogory, user_index):
    print(f"{hometown_list[user_index] if category =='H' else favorite_food_list[user_index]} ")

def main_program():

# Need to figure out how to link this to dict.
  build_database()

  while True:

    # prompt for student number
    n = prompt_for_action()

    if n == None:
      print("Thank you")
      break

    print_student_details(student_number = n)

    c = prompt_for_category()
    print_category_details(category = c, user_index = n)

# still need to create equivalent of "promt_for_continue" function
    continue_response = prompt_for_continue()
    if continue_response == 'N':
      print("\nThank you")
      break
