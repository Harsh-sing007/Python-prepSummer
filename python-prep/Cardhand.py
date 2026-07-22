# Implement a CardHand class that supports a person arranging a group of cards in his or her hand. The simulator should represent the sequence of cards using a single positional list ADT so that cards of the same suit are kept together. Implement this strategy by means of four “fingers” into the hand, one for each of the suits of hearts, clubs, spades, and diamonds, so that adding a new card to the person’s hand or playing a correct card from the hand can be done in constant time.  The class should support the following methods:  ● add_card(r, s): Add a new card with rank r and suit s to the hand. ● play(s): Remove and return a card of suit s from the player’s hand; if there is no card of suit s, then remove and return an arbitrary card from the hand.  ● __iter__(): Iterate through all cards currently in the hand.  ● all_of_suit(s): Iterate through all cards of suit s that are currently in the hand 
class CardHand:
    def __init__(self):
        self.cards = []
        self.suits = {
            "hearts": [],
            "clubs": [],
            "spades": [],
            "diamonds": []
        }

    def add_card(self, r, s):
        card = (r, s)
        self.cards.append(card)
        self.suits[s].append(card)

    def play(self, s):
        if self.suits[s]:
            card = self.suits[s].pop(0)
            self.cards.remove(card)
            return card

        elif self.cards:
            card = self.cards.pop(0)
            self.suits[card[1]].remove(card)
            return card

        return None

    def __iter__(self):
        return iter(self.cards)

    def all_of_suit(self, s):
        return iter(self.suits[s])

hand = CardHand()

hand.add_card("A", "hearts")
hand.add_card("10", "clubs")
hand.add_card("K", "hearts")
hand.add_card("7", "spades")
hand.add_card("Q", "diamonds")
hand.add_card("5", "clubs")

print("Cards in Hand:")
for card in hand:
    print(card)

print("\nPlay a Hearts card:")
print(hand.play("hearts"))

print("\nPlay a Spades card:")
print(hand.play("spades"))

print("\nPlay a Diamonds card:")
print(hand.play("diamonds"))

print("\nRemaining Cards:")
for card in hand:
    print(card)

print("\nAll Clubs:")
for card in hand.all_of_suit("clubs"):
    print(card)