# Determine whether input retrieved from the user is valid.
# Return True if
# - the word is 5 letters long
# - the word only contains characters
def test_input(user_input):
    if len(user_input) != 5:
        return False
    for char in user_input:
        if not char.isalpha():
            return False
    return True


# Get a valid input from the user and return this input.
# Should only return inputs that are valid.
# This should keep asking for input until a valid input is entered
def get_input():
    user_guess = input("Please enter your 5 letter guess: ")
    while not test_input(user_guess):
        print("You must enter a 5 letter word with no symbols or digits.")
        user_guess = input("Please enter your 5 letter guess: ")
    else:
        return user_guess


# Test whether the guess entered by the user is the same as the secret word.
# Should return True if the word is completely correct otherwise return False

# Should print out the following for each of the letters as it checks them:

# G for any letter that is in the correct place in the word
# Y for any letter which is in the word but in an incorrect position
# * for any letter which is not in the word at all.
# For example, test_word("error", "steer") # returns False and prints out **YYG to the console
def test_word(secret_word, user_guess):
    letter_index = 0
    feedback_string = ""
    while letter_index < 5:
        if user_guess[letter_index] == secret_word[letter_index]:
            # print in green if in the right place.
            feedback_string += "G"
        # test if letter in rest of word
        elif user_guess[letter_index] in secret_word:
            # print yellow if letter is in the word but in wrong position.
            feedback_string += "Y"
        else:
            feedback_string += "*"

        letter_index += 1
    print(feedback_string)

    if feedback_string == "GGGGG":
        return True
    else:
        return False


# Starts the game with a secret word passed as a parameter.
def start_game(secret_word):
    attempts = 1
    print("Welcome to Derble!")
    print("You have up to 6 attempts to guess the secret word!")
    while not test_word("error", get_input()):
        if attempts >= 6:
            print(f"The correct word was \"{secret_word}\". Better luck next time.")
        else:
            print(f"Incorrect! You have {6 - attempts} attempts remaining.")
            attempts += 1
    else:
        print(f"Congrats! You took {attempts} attempts.")




if __name__ == "__main__":
    start_game("error")