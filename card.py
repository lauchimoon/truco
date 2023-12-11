class Card:
    def __init__(self, palo, value):
        self.palo = palo
        self.value = value
        self.envido_value = 0

        if value > 0 and value < 8:
            self.envido_value = value
        else:
            self.envido_value = 0

    def __repr__(self):
        return f"p:{self.palo};v:{self.value};ev:{self.envido_value}"

