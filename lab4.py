checking = "yes"

while checking == "yes": # Loop until the user decides to stop
    print("What is your age? ") # Ask the user for their age
    user_input = input() # Read the input from the user
    if int(user_input) >= 18: # Check if the age is 18 or older
        print("Yes, you can vote.") # Prints if the user can vote
    else:
        print("No, you cannot vote.") # Prints if the user cannot vote
    
    print("Do you want to check another age? ") # Ask if the user wants to check another age
    user_input2 = input() # Read the input from the user
    checking = user_input2 # Update the checking variable based on user input

list1 = [3, -1, 0, 6, -4]

for x in list1: # Iterate through each number in the list
    if x > 0: # Check if the number is positive
        print("Value is positive") # Prints if the number is positive
    elif x < 0: # Check if the number is negative
        print("Value is negative") # Prints if the number is negative
    else: # If the number is neither positive nor negative
        print("Value is zero") # Prints if the number is zero

inventory = {"pencil", "pen", "color pencil", "marker", "crayon"}

for i in inventory: # Iterate through each time in the inventory set
    if i == "pencil": # Check if the item is "pencil"
        print("You can now write!") # Prints a message if "pencil" is found
    else: # If the item is not "pencil"
        print(f"You have {i}") # Prints the item in the inventory set


        
