from card import Card
import collections
import heapq

def calculate_envido(cards):
    envido = 0
    palos = [c.palo for c in cards]
    palo = ""

    # Find at least two of the same type
    counter = collections.Counter(palos)
    for key, value in counter.items():
        if value > 1:
            palo = key

    # If adding, add the highest of the two cards
    values = []
    for card in cards:
        if card.palo == palo:
            values.append(card.envido_value) 

    largest = heapq.nlargest(2, values)
    envido += sum(largest)

    if palo:
        envido += 20
    else:
        envido += max([c.envido_value for c in cards])

    return envido

if __name__ == '__main__':
    card_list = [Card("espada", 6), Card("oro", 7), Card("oro", 5)]
    env = calculate_envido(card_list)
    print(env)
