import random

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value,self.suit)

class Deck:
    def __init__(self):
        suits=["Hearts","Diamonds","Clubs","Spades"]
        values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card(value,suit) for suit in suits for value in values ]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self,request):
        if self.count() == 0:
            raise ValueError ("All cards have been dealt")
        actualdeal = min(request, len(self.cards))
        cards = self.cards[-actualdeal:]
        self.cards=self.cards[:-actualdeal]
        return cards

    def shuffle(self):
        if Deck.count(self) != 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.cards)
        return self.cards

    def deal_card(self):
        return self._deal(1)[0]


    def deal_hand(self,r):
        return self._deal(r)
    #     return c

d = Deck()
print(d)
# print(d.cards)
# #print(d.deal_card())
# print(d.deal_hand(5))
