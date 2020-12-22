import re

# extract input from file
with open('input.txt', 'r') as f:
    p1, p2 = [[int(i) for i in re.findall(r'\d+', x)[1:]] for x in (f.read() + '\n').split('\n\n')]

# game ends when one of the players is out of cards
while len(p1) > 0 and len(p2) > 0:    
    # both players remove their top card
    a = p1.pop(0)
    b = p2.pop(0)
    if a > b:
        # player 1 win
        p1 += [a, b]
    else:
        # player 2 win
        p2 += [b, a]

# calculate answer
winning_deck = p1 if len(p2) == 0 else p2
winning_deck_length = len(winning_deck)
winning_score = sum([x * (winning_deck_length - i) for i, x in enumerate(winning_deck)])
print(winning_score)
