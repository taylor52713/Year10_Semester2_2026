# Error Checking
# Taylor Botha
# 14 Oct 2026

# Code that that tests whether a valid input was given (V1)
'''done = True # Boolean variable set to true
while done:
    num = int(input("Please enter your value as an integer: "))
    done = False

print(f"The number you entered is {num}")'''

#Using a try and except method to check for valid input (V1.1)
#Use try and except method to catch errors
done = False
while not done:
    try: #This method tries for a valid input
        num = float(input("Please enter a number: "))
        done  = True

    except ValueError:
        print("That is not a valid float number. \n")

print(f"The number you entered is {num}.")


