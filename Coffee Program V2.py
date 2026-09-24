# Creating a coffee program that a user will be able to interact with.
# Taylor Botha
# 23 Sep 2026
# Version 1

# TODO: Record and input (Store the answer)
#       Check for valid answer (Input checkker)
#       Ask questions and respond

'''# Ask the user whether they like coffe or not
like_coffee = input("Do you like coffee? ")
print(like_coffee) # Checking the input is stored
print(f"Your answer was '{like_coffee}'")

# Check the input and response(to be fixed next time)
if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee == "Y" or like_coffee == "yeah" or like_coffee == "Yeah":
    print("That is great! I like coffee too.")
else:
    print("You are missing out! Why not give it a try?")'''

#Version 2
#While loop to test the program
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ")
    print(like_coffee) # Checking the input is stored
    print(f"Your answer was '{like_coffee}'")

    #Check the input and respond 
    if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee == "Y" or like_coffee == "yeah" or like_coffee == "Yeah":
        print("That is great! I like coffee too.")
        keep_going = "Finish"
    elif like_coffee == "NO" or like_coffee == "no" or like_coffee == "N" or like_coffee == "n":
        print("You are missing out! Why not give it a try?")
        keep_going ="hufwgjfkhlhuiwhfwdsiwu"
    else:
        print("I don't understand. Please try again.")

  

