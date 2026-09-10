class Card:
    def __init__(self, rank, suit):
        self.value = (rank, suit)

    def display_info(self):
        rank = self.value[0]
        suit = self.value[1]

        result = f"{rank} of {suit}"
        return result

if __name__ == "__main__":
    card = Card("A", "Hearts")
    print(card.display_info())