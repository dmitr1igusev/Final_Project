class FlashCard:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2


class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, index):
        del self.cards[index]

    def modify_card(self, index, card):
        self.cards[index] = card
