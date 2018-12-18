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


class Game:
  def __init__(self):
    self.deck = Deck()
    p1 = Player('AI-1', self.deck.cards[0:13])
    p2 = Player('AI-2', self.deck.cards[13:26])
    p3 = Player('AI-3', self.deck.cards[26:39])
    p4 = Player('AI-4', self.deck.cards[39:52])
    self.players = [p1, p2, p3, p4]
    #self.trump = t #not needed yet


  def play_out(self):
    #implemented this with a counter now, moight be better with a boolean 'active'?
    tricks_played = 0
    for i in range(13):
      for p in self.players:
        print(p.name, 'plays', p.play_random_card())



def main():
  g = Game()
  g.play_out()



if __name__ == '__main__':
  main()
