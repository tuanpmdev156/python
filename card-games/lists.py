"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
import statistics

def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    # 1st solution
    # all_round_list = []
    # for item1 in rounds_1:
    #     all_round_list.append(item1)
    # for item2 in rounds_2:
    #     all_round_list.append(item2)
    # return all_round_list
    
    # 2nd solution
    # round_1.extend(round_2)
    # return round_1
    
    # 3rd solution
    return rounds_1 + rounds_2
    

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    # 1st solution
    # if len(rounds) > 0:
    #     for item in rounds:
    #         if item == number:
    #             return True
    # return False
    
    # 2nd solution
    #return number in rounds
    
    # 3rd solution
    #return rounds.count(number) > 0

    # 4th solution
    rounds_set = set(rounds)
    return number in rounds_set


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    # 1st solution
    # if not hand:
    #     return 0 # Prevent ZeroDivisionError if the list is empty
    # return sum(hand)/len(hand)
    
    # 2nd solution
    if not hand:
        return 0  # Prevent ZeroDivisionError if the list is empty
    return statistics.mean(hand) 


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    # 1st solution: Assigning temporary variables + Set{}
    # average_of_card = card_average(hand)
    # first_and_last_average = (hand[0] + hand[-1])/2
    # median_value = hand[int(len(hand) / 2)]
    # return average_of_card in {median_value,first_and_last_average}
    
    # 2st solution: Short-circuiting (Most efficient)
    # avg = card_average(hand)
    # if (hand[0] + hand[-1])/2 == avg:
    #     return True
    # return hand[len(hand) // 2] == avg

    # 3rd solution: (One-liner - Most concise) + Tuple()
    return card_average(hand) in ((hand[0] + hand[-1])/2,hand[len(hand) // 2])


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    # 1st solution: Create sliced sublists
    # odds = hand[0::2]
    # evens = hand[1::2]
    # return card_average(odds) == card_average(evens)

    # 2nd solution: For loop and index tracker
    # even_sum, odd_sum, even_count, odd_count = 0,0,0,0
    # for index,card in enumerate(hand):
    #     if index % 2 == 0:
    #         even_sum += card
    #         even_count += 1
    #     else:
    #         odd_sum += card
    #         odd_count += 1
    # return (even_sum / even_count) == (odd_sum / odd_count)

    # 3rd solution : Cross-Multiplication (Most efficient)
    odds = hand[0::2]
    evens = hand[1::2]
    return sum(odds) * len(evens) == sum(evens) * len(odds)

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    # 1st solution: 
    # Data Safety: Medium-Low (Inconsistent; returns original OR copy)
    # Memory efficiency: High (If not 11); Medium (If 11)
    # last = hand[-1]
    # if last != 11:
    #     return hand
    # new_hand = hand[0:-1]
    # new_hand.append(last*2)
    # return new_hand

    # 2nd solution: 
    # Data Safety: Dangerous (Permanently mutates original input)
    # Memory efficiency: Highest (Zero new lists created)
    # if hand[-1] == 11:
    #     hand[-1] = 22
    # return hand

    # 3rd solution:
    # Data Safety: Safe (Always returns a fresh, isolated copy)
    # Memory efficiency: Medium (Always creates a new list)
    # last_card = hand[-1] * 2 if hand[-1] == 11 else hand[-1]
    # return hand[:-1] + [last_card]

    # 4nd solution:
    # Data Safety: Safe (Always returns a fresh, isolated copy)
    # Memory efficiency: Medium (Always creates a new list)
    new_hand = hand.copy()
    if new_hand[-1] == 11:
        new_hand[-1] = 22
    return new_hand