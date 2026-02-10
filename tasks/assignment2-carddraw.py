# assignment 2: Write a program that "deals" (prints out) 5 cards, congratulate the user if the get a good hand 
# date: 2026-02-10
# author: irene celebrin 

import requests
from collections import Counter 

# shuffle deck (1 is enough)
shuffle_url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?'
shuffle_parameters = {
    'deck_count': 1}

# get response and read it as json 
shuffle_response = requests.get(shuffle_url, params=shuffle_parameters).json()
# get deck id
deck_id = shuffle_response["deck_id"]

# draw 5 cards (it's also posisble to shuffle and draw the same time,  replace <<deck_id>> with "new")
draw_url = 'https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/'
draw_parameters = {
    'count': 5
}

draw_response = requests.get(draw_url, params=draw_parameters).json()

print("Your hand:")
cards = draw_response["cards"]
values = []
suits = []
for card in cards:
    print(card["value"] + " of " + card["suit"])
    values.append(card["value"])
    suits.append(card["suit"])

# count counts for each value with Counter. see: https://www.geeksforgeeks.org/python/python-counter-objects-elements/
value_count = Counter(values)
# print congratulations for pairs and triples 
for value, count in value_count.items():
    if count == 4:
        print("Congratulations! You got four of a kind!")
    elif count == 3:
        print("Congratulations! You got three of a kind!")
    elif count == 2:
        print("Congratulations! You got a pair!") # option: add which value : f"Congratulations! You got a pair of {value}!"


# remap to numbers and make them integers 
for value in values:
    if value == "ACE":
        values[values.index(value)] = 14
    elif value == "KING":
        values[values.index(value)] = 13
    elif value == "QUEEN":
        values[values.index(value)] = 12
    elif value == "JACK":
        values[values.index(value)] = 11
    else:
        values[values.index(value)] = int(value)

# sort values 
sorted_values = sorted(values)
# check for straight: if the difference between the highest and lowest value is 4 and there are 5 unique values, then it's a straight
if sorted_values[4] - sorted_values[0] == 4 and len(set(sorted_values)) == 5:
    print("Congratulations! You got a straight!")


# check suit 
if len(set(suits)) == 1:
    print("Congratulations! You got a flush!")

#TODO: reset code so that all checks are performed at the same time

