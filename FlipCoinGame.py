'''
 * Alice and Bob  - flip coin game:
 * Strategy 1. Alice calls a random number - Probability ½
 * Strategy 2. Alice calls 1 and Bob calls 1 - Probability ¾
 * Strategy 2A. Alice calls 0 and Bob calls 0 - Probability ¾
 * Strategy 3. Everyone says that he (she) received - Probability ½
 * Strategy 4. Alice calls that she got and
 * 			   Bob calls the opposite of what he received -
 * 			   Probability 1
'''

from random import randint
from operator import xor


def flip_coin():
    '''
    Method that returns 0 or 1 randomly.
    :return: 0 or 1 randomly
    '''
    # Return a random integer between 0 and 1 using the randint function from the random module
    return randint(0, 1)

def alice_game():
    '''
    Method that returns the result of Alice's game.
    :return: 0 or 1 randomly
    '''
    # Return the result of calling the flip_coin function
    return flip_coin()

def bob_game():
    '''
    Method that returns the result of Bob's game.
    :return: 0 or 1 randomly
    '''
    # Return the result of calling the flip_coin function
    return flip_coin()

# Alice calls a random number - Probability 0.5
def game_strategy1():
    '''
    Method that returns the result of Alice's game strategy where Alice calls a random number.
    The probability of Alice winning is 0.5.
    :return: True if Alice wins, False if Alice loses
    '''
    # Call the alice_game function to get the result of Alice's game
    result = True if alice_game() > 0 else False
    # Return the result
    return result

# Alice calls 1 and Bob calls 1 - Probability 0.75
# symmetric: Alice calls 0 and Bob calls 0

def game_strategy2():
    '''
    Method that returns the result of Alice's game strategy where Alice calls 1 and Bob calls 1.
    The probability of Alice winning is 0.75.
    :return: True if Alice wins, False if Alice loses
    '''
    # Call the alice_game and bob_game functions to get the results of Alice's and Bob's games
    result = True if alice_game() == 1 or bob_game() == 1 else False
    # Return the result
    return result

# Everyone says that s/he received - Probability 0.5
def game_strategy3():
    '''
    Method that returns the result of Alice's game strategy where everyone says that they received their coin.
    The probability of Alice winning is 0.5.
    :return: True if Alice wins, False if Alice loses
    '''
    # Call the alice_game and bob_game functions to get the results of Alice's and Bob's games
    result = True if alice_game() == bob_game() else False
    # Return the result
    return result

# Alice calls that she got, Bob calls the opposite of what he received - Probability 1
def game_strategy4():
    '''
    Method that returns the result of Alice's game strategy where Alice calls that she received her coin,
    and Bob calls the opposite of what he received.
    The probability of Alice winning is 1.
    :return: True if Alice wins, False if Alice loses
    '''
    # Call the alice_game and bob_game functions to get the results of Alice's and Bob's games
    alice, bob = alice_game(), bob_game()
    # Use the xor function to determine if Alice wins
    result = True if (alice == bob) or xor(bob, alice) else False
    # Return the result
    return result

def main():
    '''
    Main function that runs the game strategies and calculates the probability of Alice winning.
    '''
    # Number of times to run the game strategies
    count = 1000000
    # List to store the number of times Alice wins for each strategy
    strategy_lst = [0] * 4  # [0,0,0,0]
    # Loop through the game strategies count number of times
    for i in range(count):
        # Increment the number of times Alice wins for each strategy
        strategy_lst[0] += game_strategy1()
        strategy_lst[1] += game_strategy2()
        strategy_lst[2] += game_strategy3()
        strategy_lst[3] += game_strategy4()
    # Loop through the strategies
    for i in range(len(strategy_lst)):
        # Calculate the probability of Alice winning for each strategy and print it
        print(f"Strategy{i + 1} probability ==>", strategy_lst[i] / count)

if __name__ == '__main__':
    main()
