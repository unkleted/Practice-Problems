# Problem 54

# In the card game poker, a hand consists of five cards and are ranked, from 
# lowest to highest, in the following way:
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest 
# value wins; for example, a pair of eights beats a pair of fives (see example 
# 1 below). But if two ranks tie, for example, both players have a pair of 
# queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:
# Hand	 	Player 1	     	Player 2	 	    Winner
# 1	 	    5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
#           Pair of Fives       Pair of Eights
# 
# 2 	 	5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
#           Highest card Ace    Highest card Queen
# 	 	
# 3	     	2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
#           Three Aces          Flush with Diamonds
# 	 	
# 4 	 	4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
#           Pair of Queens      Pair of Queens
#           Highest card Nine   Highest card Seven
# 	 	
# 5	 	    2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
#           Full House          Full House
#           With Three Fours    with Three Threes
# 	 	
# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): the 
# first five are Player 1's cards and the last five are Player 2's cards. You 
# can assume that all hands are valid (no invalid characters or repeated cards), 
# each player's hand is in no specific order, and in each hand there is a clear 
# winner.

# How many hands does Player 1 win?

from collections import Counter

class Hand:
    card_value_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }


    def __init__(self, card_string):
        # Parse cards
        self.values = [Hand.card_value_map[c[0]] for c in card_string.split()]
        self.suits = {c[1] for c in card_string.split()} # set of suits

        # Precompute helpers
        self.counts = Counter(self.values) # value -> frequency
        self.num_of_each_card = tuple(sorted(self.counts.values(), reverse=True))
        self.card_values = tuple(sorted(self.values, key=lambda v: (self.counts[v], v), reverse=True))
        
        # Score the hand
        self.score = self.score_hand()


    def score_hand(self):
        if self.royal_flush():
            return (9,) + self.card_values
        elif self.straight_flush():
            return(8,) + self.card_values
        elif self.four_of_a_kind():
            return(7,) + self.card_values
        elif self.full_house():
            return(6,) + self.card_values
        elif self.flush():
            return(5,) + self.card_values
        elif self.straight():
            return(4,) + self.card_values
        elif self.three_of_a_kind():
            return(3,) + self.card_values
        elif self.two_pair():
            return(2,) + self.card_values
        elif self.one_pair():
            return(1,) + self.card_values
        else:
            return(0,) + self.card_values


    def royal_flush(self) -> bool:
        con1 = self.card_values == (14,13,12,11,10)
        return con1 and self.flush()


    def straight_flush(self) -> bool:
        return self.flush() and self.straight()


    def four_of_a_kind(self) -> bool:
        return self.num_of_each_card == (4,1)


    def full_house(self) -> bool:
        return self.num_of_each_card == (3,2)


    def flush(self) -> bool:
        return len(self.suits) == 1
        

    def straight(self) -> bool:
        con1 = self.num_of_each_card == (1,1,1,1,1)
        con2 = max(self.card_values) - min(self.card_values) == 4
        return con1 and con2


    def three_of_a_kind(self) -> bool:
        return self.num_of_each_card == (3,1,1)
        

    def two_pair(self) -> bool:
        return self.num_of_each_card == (2,2,1)
        

    def one_pair(self) -> bool:
        return self.num_of_each_card == (2,1,1,1)
      

    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score


wins = 0

filename = "text files/0054_poker.txt"
try:
    with open(filename, 'r') as file_object:
        for line in file_object:
            cards = line.strip().split()
            h1, h2 = " ".join(cards[:5]), " ".join(cards[5:])
            player1 = Hand(h1)
            player2 = Hand(h2)

            if player1 > player2:
                wins += 1

except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(wins)