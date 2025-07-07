# Lab 5 Wilson Pham

def cat_greeting(word):
    print(f"Cat says {word}!")
    print("Cat sees Wilson!")

cat_greeting("Meow")

def generate_superhero_power():
    name = "Wilson"
    power = "invisibility"
    print(f"{name} has the power of {power}!")

generate_superhero_power()

def generate_superhero_power1():
    power = "Super Strength"
    return power

print(generate_superhero_power1())

def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message

print(generate_superhero_power2("Wilson", "Super Speed"))

def cat_greetings_loop(greeting):
    for i in range(5):
        print(f"Cat says {greeting}")

cat_greetings_loop("Meow")

def generate_multiple_powers():
    superpowers = ["Flying", "Invisibility", "Super Strength", "Telepathy"]
    for i in superpowers:
        print(f"Superpower: {i}")

generate_multiple_powers()
