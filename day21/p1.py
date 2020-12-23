from functools import reduce

# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

# can only deduce that for each allergen, all the missing ingredients are not it
all_ingredients = set()
all_allergens = set()
food_info = []
ingredient_freq = {}
for line in lines:
    # extract data
    ingredients, allergens = line[:-1].split(' (contains ')
    ingredients = set(ingredients.split(' '))
    allergens = set(allergens.split(', '))
    # update corresponding data structures
    all_ingredients |= ingredients
    all_allergens |= allergens
    food_info.append((ingredients, allergens))
    for ingredient in ingredients:
        ingredient_freq[ingredient] = ingredient_freq.get(ingredient, 0) + 1

# safe: allergens -> ingredients
safe = {}
for ingredients, allergens in food_info:
    missing_ingredients = all_ingredients - ingredients
    for allergen in allergens:
        safe[allergen] = safe.get(allergen, set()) | missing_ingredients

# the safe ingredients (definitely not it) are safe from all allergens
safe_ingredients = reduce(lambda x, y: x & y, safe.values())
print(sum([ingredient_freq[ingredient] for ingredient in safe_ingredients]))
