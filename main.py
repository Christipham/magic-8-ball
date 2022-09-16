# Import random module using the import keyword
import random

# Create a function say codeMagic_8ball() (Which is used to Implement the main logic of the magic 8 ball program)
def codeMagic_8ball():
    # Give the response you want as user input using the input() function and
    # store it in a variable
    User_response = input("Enter any yes or no question for answer and 'quit' to exit:")
    # Give the list of all eight ball answers and store it in another variable
    Magic_8ball_answers = [
        "From my sources, absolutely",
        "Unfortunately nahh",
        "You gotta concentrate, ask again",
        "My mind is a bit fuzzy, come back later",
        "Yasss, definitely",
        "Don't cry, the answer is no",
        "I believe so",
        "Don't kid urself",
        "stay calm and say it again",
        "yeaa",
        "no, just no",
        "is my dog named cat? ",
        "ofc the answer would be yes",
        "close the computer and try again",
        "turn it off and on again",
        "be more specific",
        "according to online laws of aviation..yes",
        "You wish",
        "U don't sound confident, try again",
        "When the world ends yeas",
        "duh",
        "stop being so nosy",
        "why u asking?",
        "yea..no",

        ]
    # Check if the obtained/input response is "quit" using the if conditional statement
    if User_response == "quit":
        # If it is true then print Some Random Acknowledgement indicating the Game is over.
        print("The Game is Ended <!!>")
    else:
        # Else print some random answer from the above given list of answers using the
        # choice() function of the random module by Passing the about Eight answers list to choice Function
        # Here \n is used a separator to Print the new line
        print(random.choice(Magic_8ball_answers), "\n")
        # Call the above created codeMagic_8ball() function Recursively to Play the Game Again.
        codeMagic_8ball()
# Call the above created codeMagic_8ball() function to start the game.
codeMagic_8ball()
