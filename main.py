numbers = [1, 2, 5]
print(5 in numbers)
print(5 not in numbers)

cities = ["Kiev", "London", "Los Angeles"]

for city in cities:
  print(city)

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
  if number > 42:
    break
  print(number)

import random
numbers = []

while len(numbers) < 5:
  numbers.append(random.randint(1, 100))

for number in numbers:
  print(number)
  if number >= 90:
    print('Found at least one number greater than 90')
    break
else:
  print('No numbers greater than 90')

print('Complete')

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
  for rank in ranks:
    print(f'{rank} of {suit}') 

    numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number = random.choice(numbers)
print(selected_number)

selected_numbers = random.choices(numbers, k=3)
print(selected_numbers)

import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} cards in the deck.')

print('Dealing ...')

hand = []

while len(hand) < 5:
    card = random.choice(deck)
    deck.remove(card)
    hand.append(card)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)