# Lab 6 by Tom Picciano


# encoder function
def encoder_function(password):
    encoded_string = ""

    for item in password: # for each value in the given password

        item = int(item) + 3  # adds the value by 3

        if item == 10: # if the password encoded value was 7 + 3 = 10
            item = 0 # gives a 0

        if item == 11: # if the password encoded value was 8 + 3 = 11
            item = 1 # gives a 1


        if item == 12: # if the password encoded value was 9 + 3 = 12
            item = 2 # gives a 2

        encoded_string += str(item) # adds the value back to the string

    return encoded_string # returns the completed string



# decoder function for partner Tre Huang


if __name__ == '__main__':

    # continue looping the program
    while True:

        # print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # get user input for menu option
        user_input = int(input("Please enter an option: "))

        # encode password. Store user input for later use
        if user_input == 1:
            user_password = int(input("Please enter your password to encode: "))
            encoded_password = encoder_function(str(user_password))
            print("Your password has been encoded and stored!")


        # user_input 2 for partner Tre Huang


        if user_input == 3:
            break