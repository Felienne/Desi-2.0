import random

class Card:
  def __init__(self, s, v):
    self.suit = s
    self.value = v

  def __str__(self):
    return self.suit + self.value



class Deck:
  suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

  def __init__(self):
    self.cards = []

    for s in Deck.suits:
      for v in Deck.values:
        c = Card(s, v)
        self.cards.append(c)
    random.shuffle(self.cards)

  def __str__(self):
    return ', '.join([str(c) for c in self.cards])


