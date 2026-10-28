# Fence cost calculator
# Taylor Botha
# 23/10/26

# Ask the user for width, length and cost per meter
# and loop until their input is higher than zero

def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True: 

        try:
            # Ask the user for a number
            response = float(input(question))

            # Check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error) 


# Main Routine:

# Display wlecome message 
print(f"Welcome to the Taylor's Fence Cost Calaculator! Please enter your measurement and prices below.")
print()

keep_going = ""
while keep_going == "":

    # Get width, length and cost per meter
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost per meter: $")

    # Calculate perimeter and cost
    perimeter = 2 * (width + length)
    price = perimeter * cost 

    
  # Display output
    print()
    print(f"Perimeter: {perimeter} meters ")
    print(f"Total cost: ${price:.2f} ")  

    # Ask the user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit: ")
    print()
    
print("Thank you for using the Fence cost calculator")

