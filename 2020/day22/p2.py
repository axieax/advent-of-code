def recursive_combat(p1, p2):
    ''' returns tuple: (winning_deck, winner) '''
    seen = set()
    while len(p1) > 0 and len(p2) > 0:
        # loop prevention
        if (tuple(p1), tuple(p2)) in seen:
            return p1, 'p1'
        seen.add((tuple(p1), tuple(p2)))
        
        # draw from top of deck
        a = p1.pop(0)
        b = p2.pop(0)
        winner = 'p1' if a > b else 'p2'

        # recursive sub game
        if len(p1) >= a and len(p2) >= b:
            winner = recursive_combat(p1[:a], p2[:b])[1]

        # update decks
        if winner == 'p1':
            p1 += [a, b]
        else:
            p2 += [b, a]

    # determine winner
    return (p1, 'p1') if len(p2) == 0 else (p2, 'p2')

if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        p1, p2 = [[int(i) for i in x.split('\n')[1:] if i] for x in (f.read() + ('\n')).split('\n\n')]
        # p1, p2 = [[int(i) for i in re.findall(r'\d+', x)[1:]] for x in (f.read() + '\n').split('\n\n')]

    # calculate answer
    winning_deck = recursive_combat(p1, p2)[0]
    winning_deck_length = len(winning_deck)
    winning_score = sum([x * (winning_deck_length - i) for i, x in enumerate(winning_deck)])
    print(winning_score)
