# Width and Height
# Taylor Botha
# 21/10/26

#Ask user for a width and loo until they 
# enter a number this is more than zero
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

#Main routine
for item in range(0, 2):
    width = num_check("Width:")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height:")
    print(height)