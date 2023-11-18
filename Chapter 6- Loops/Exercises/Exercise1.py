# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Start the loop
while True:
    # Prompt the user to enter a topping
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered

    # Add the topping to the list
    pizza_toppings.append(topping)

    # Print a message saying the topping will be added to the pizza
    print(f"Adding {topping} to your pizza.")

# Print the final list of pizza toppings
print("\nYour pizza toppings:")
for topping in pizza_toppings:
    print(topping)
