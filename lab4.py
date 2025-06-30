#checking = "yes"

#while checking == "yes": 
    #print("What is your age? ")
    #user_input = input()
    #if int(user_input) >= 18:
        #print("Yes, you can vote.")
    #else:
        #print("No, you cannot vote.")
    
    #print("Do you want to check another age? ")
    #user_input2 = input()
    #checking = user_input2

#list1 = [3, -1, 0, 6, -4]

#for x in list1:
    #if x > 0:
        #print("Value is positive")
    #elif x < 0:
        #print("Value is negative")
    #else:
        #print("Value is zero")

inventory = {"tnt", "glass", "grass", "netherite", "Waxed Lightly Weathered Chiseled Copper Stairs"}

for i in inventory: # Iterate through each time in the inventory set
    if i == "netherite": # Check if the item is "neitheriote"
        print("You have found the most powerful block in Minecraft!") # Prints a message if "netherite" is found
    else: # If the item is not "netherite"
        print(f"You have {i}") # Prints the item in the inventory set


        
