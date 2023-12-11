import card
import player
import random

class Game:
    def __init__(self):
        self.cards = []
        self.players = [player.Player([]), player.Player([])]

    def gen_cards(self):
        palos = ["oro", "espada", "basto", "copa"]

        for palo in palos:
            for n in range(1, 13):
                if n != 8 and n != 9:
                    c = card.Card(palo, n)
                    g.cards.append(c)

    def shuffle_cards(self):
        for i in range(0, len(self.players)):
            for _ in range(0, 3): # do this 3 times
                random_card = random.choice(self.cards)
                self.players[i].cards.append(random_card)
                self.cards.remove(random_card)

g = Game()
g.gen_cards()
g.shuffle_cards()

for player in g.players:
    print(player.cards)
