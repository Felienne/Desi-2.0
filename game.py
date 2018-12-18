from deck import Deck
import random

def cards_in_suit(cards, suit):
  return [c for c in cards if c.suit == suit]


def highest_card_in_suit(cards, suit):
  max_card_value = max([c.get_integer_value() for c in cards if c.suit == suit])
  #todo: regel hierboven kan ook cards_in_suit() gebruiken
  # get the corresponding card (indexing is safe, there can only be one)
  highest_card = [c for c in cards if c.get_integer_value() == max_card_value and c.suit == suit][0]
  return highest_card


class Trick:

  #a trick receives 4 cards and decides who won based on the cards and the trump suit
  def __init__(self, t, c = []):
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
      trump_cards = [c for c in self.cards if c.suit == self.trump] #observation: I guess this would work alone too (because there would not be cards with SA as trump color :)

    if trump_cards == []:
      #determine the highest value
      highest_card = highest_card_in_suit(self.cards, start_suit)

      #simply return the player number of the highest card
      owner_of_highest_card = self.cards.index(highest_card)

    else:
      #if there are trumps, get the highest trump card
      #determine the highest value
      highest_card = highest_card_in_suit(self.cards, self.trump)

      #simply return the player number of the highest card
      owner_of_highest_card = self.cards.index(highest_card)

    return owner_of_highest_card


class Player:
  def __init__(self, n, h):
    self.name = n
    self.hand = h

  def play_random_card(self):
    card = random.choice(self.hand)
    self.hand.remove(card)
    return card

  def play_based_on_trick(self, t: Trick):
    if t.cards == []: #first player? play random!
      return self.play_random_card()
    else:
      #filter cards based on start suit
      cards_in_start_suit = cards_in_suit(self.hand, t.cards[0].suit)


      if cards_in_start_suit == []:
        return self.play_random_card() #no start suit? draw random!
      else:
        card = random.choice(cards_in_start_suit)
        self.hand.remove(card)
      return card





class Game:
  def start_player_now(self, player_num):
    # this method reorganizes the player list according to a winner
    # given as integer

    if player_num != 0:
      # we don't have to change anything if the first player won the trick, they just remain first
      start_part = self.players[player_num:] #we start at the player that gets tp start
      remaining_part = self.players[:player_num] #we glue the rest at the end
      self.players = start_part + remaining_part


  def __init__(self):
    self.deck = Deck()
    p1 = Player('AI-1', self.deck.cards[0:13])
    p2 = Player('AI-2', self.deck.cards[13:26])
    p3 = Player('AI-3', self.deck.cards[26:39])
    p4 = Player('Felienne', self.deck.cards[39:52])
    self.players = [p1, p2, p3, p4]
    #self.trump = t #not needed yet


  def play_out(self):
    # implemented this with a counter now, might be better with a boolean 'active'?


    for i in range(13):
      trick = Trick('Clubs')
      trick.cards = []

      for p in self.players:
        card_played = p.play_based_on_trick(trick)
        trick.cards.append(card_played)

      winner = trick.winner()

      print([str(c) for c in trick.cards], winner)

      self.start_player_now(winner)
      print([p.name for p in self.players])

      # for p in self.players:
      #   print(p.name, 'plays', p.play_random_card())



def main():
  g = Game()
  g.play_out()



if __name__ == '__main__':
  main()
