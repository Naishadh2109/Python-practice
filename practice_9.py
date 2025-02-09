import random

# coin = random.choice(["Heads", "Tails"])
# print(coin)

# number = random.randint(1, 6)
# print(number)

cards = ["Jack Of Hearts", "Queen Of Hearts", "King Of Hearts", "Ace Of Hearts", "Jack Of Spades", "Queen Of Spades", "King Of Spades", "Ace Of Spades"]
random.shuffle(cards)
for card in cards:
    print(card)