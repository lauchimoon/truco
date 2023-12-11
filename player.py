import card
import heapq
import collections

class Player:
    def __init__(self, cards):
        self.cards = cards
        self.envido = 0

    def calc_envido(self):
        palos = [c.palo for c in self.cards]
        palo = ""

        # Find at least two of the same type
        counter = collections.Counter(palos)
        for key, value in counter.items():
            if value > 1:
                palo = key

        # If adding, add the highest of the two cards
        values = []
        for c in self.cards:
            if c.palo == palo:
                values.append(c.envido_value) 

        largest = heapq.nlargest(2, values)
        self.envido += sum(largest)

        if palo:
            self.envido += 20
        else:
            self.envido += max([c.envido_value for c in self.cards])

