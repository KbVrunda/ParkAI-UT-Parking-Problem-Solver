import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #return function
    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = []
        #adding all combinations to an empty deck
        for s in suit:
            for v in value:
                self.deck.append(Card(s,v))

    #return function
    def __repr__(self):
        #counting the number of cards left in the deck
        cards_left = int(len(self.deck))
        return f"Cards remaining in deck: {cards_left}"

    def shuffle(self):
        #makes sure the deck of cards has all 52 cards and then rearranges them randomly
        random.shuffle(self.deck)

    def deal(self):
        #deal a single card from the deck (think pop)- after the card is dealt it is removed from the deck
        card = self.deck.pop()
        return card

if __name__ == "__main__":
    d1 = Deck()
    d1.shuffle()
    print(d1.deal())
    print(d1.deal())
    print(d1)