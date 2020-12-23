from functools import reduce

# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

# can only deduce that for each allergen, all the missing ingredients are not it
all_ingredients = set()
all_allergens = set()
food_info = []
for line in lines:
    # extract data
    ingredients, allergens = line[:-1].split(' (contains ')
    ingredients = set(ingredients.split(' '))
    allergens = set(allergens.split(', '))
    # update corresponding data structures
    all_ingredients |= ingredients
    all_allergens |= allergens
    food_info.append((ingredients, allergens))

# safe: allergens -> ingredients
safe = {}
for ingredients, allergens in food_info:
    missing_ingredients = all_ingredients - ingredients
    for allergen in allergens:
        safe[allergen] = safe.get(allergen, set()) | missing_ingredients

# the safe ingredients (definitely not it) are safe from all allergens
safe_ingredients = reduce(lambda x, y: x & y, safe.values())

# possible: allergens -> ingredients
possible = {}
for allergen, ingredients in safe.items():
    # possible ingredients are the ones which are not safe (and not definitely safe)
    possible[allergen] = all_ingredients - ingredients - safe_ingredients

# Find unique ingredient for each allergen
eliminated = set()
while True:
    unique_allergens = 0
    for allergen, ingredients in possible.items():
        if len(ingredients) == 1:
            # specify the ingredient as unique
            eliminated |= ingredients
            unique_allergens += 1
        else:
            # remove eliminated ingredients
            possible[allergen] -= eliminated
    # exit when all allergens match to a unique ingredient
    if unique_allergens == len(all_allergens):
        break

# extract single member from set by list(set)[0]
print(','.join([list(ingredient)[0] for allergen, ingredient in sorted(possible.items(), key=lambda pair: pair[0])]))
