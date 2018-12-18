from deck import Deck
import random

class Player:
  def __init__(self, n, h):
    self.name = n
    self.hand = h

  def play_random_card(self):
    card = random.choice(self.hand)
    self.hand.remove(card)
    return card

class Trick:



  #a trick receives 4 cards and decides who won based on the cards and the trump suit
  def __init__(self, c, t):
    self.cards = c
    self.trump = t

  def winner(self):
    #todo: this is not very efficient, it can be done with one run over the list of cards
    #could add up if we start MCTS

    #gevraagde kleur (TODO: wat is dat in het Engels?)
    start_suit = self.cards[0].suit

    #are there any trump cards or is the bid NoTrump?
    if self.trump == "SA":
      trump_cards = []
    else:
      trump_cards = [c for c in self.cards if c.suit == self.trump]

    if trump_cards == []:
      #determine the highest value
      max_card_value = max([c.get_integer_value() for c in self.cards if c.suit == start_suit])

      #get the corresponding card (indexing is safe, there can only be one)
      highest_card = [c for c in self.cards if c.get_integer_value() == max_card_value and c.suit == start_suit][0]

      #simply return the player number of the highest card
      owner_of_highest_card = self.cards.index(highest_card)

    #TODO: take trump into account

    return owner_of_highest_card



class Game:
  def __init__(self):
    self.deck = Deck()
    p1 = Player('AI-1', self.deck.cards[0:13])
    p2 = Player('AI-2', self.deck.cards[13:26])
    p3 = Player('AI-3', self.deck.cards[26:39])
    p4 = Player('Felienne', self.deck.cards[39:52])
    self.players = [p1, p2, p3, p4]
    #self.trump = t #not needed yet


  def play_out(self):
    #implemented this with a counter now, might be better with a boolean 'active'?
    tricks_played = 0
    for i in range(13):
      #create a trick by letting each player create a cards
      cards_in_trick = [p.play_random_card() for p in self.players]

      t = Trick(cards_in_trick, 'SA')
      print([str(c) for c in t.cards], t.winner())

      # for p in self.players:
      #   print(p.name, 'plays', p.play_random_card())



def main():
  g = Game()
  g.play_out()



if __name__ == '__main__':
  main()
