# Higher or Lower game
import random
# Import data from data.py
from data import data
# Import log and vs from art.py
from art import logo, vs

print(logo)


def get_random_account():
    """Returns a random account from game data."""
    return random.choice(data)


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def compare_followers(a_followers, b_followers):
    """Compare the follower count of two accounts."""
    if a_followers > b_followers:
        return "a"
    else:
        return "b"


def higher_lower_game():
    """Higher or Lower game."""
    # Initialise score and game control variable
    score = 0
    game_should_continue = True

    # Get the initial accounts
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Move account B to account A and get a new account for B
        account_a = account_b
        account_b = get_random_account()

        # Ensure the new account B is different from account A
        while account_a == account_b:
            account_b = get_random_account()

        # Display the accounts' details
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        # Ask the player for their guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get the follower counts for both accounts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if the player's guess is correct
        is_correct = compare_followers(a_follower_count, b_follower_count) == guess

        if is_correct:
            # Increase the score if the guess is correct
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            # End the game if the guess is incorrect
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

# Start the game
higher_lower_game()