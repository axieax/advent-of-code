from functools import reduce

# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

# map from food to ingredients
recipe = {}
# map from ingredients to food
i_f = {}
# map from possible allergen to foods
a_f = {}

all_ingredients = set()
for food, line in enumerate(lines):
    # extract data
    ingredients, allergens = line[:-1].split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.split(', ')
    all_ingredients = all_ingredients.union(set(ingredients))
    # mapping from possible allergen to foods
    for allergen in allergens:
        a_f[allergen] = a_f.get(allergen, []) + [food]
    # mapping from food to ingredients
    recipe[food] = set(ingredients)
    # mapping from ingredient to foods
    for ingredient in ingredients:
        i_f[ingredient] = i_f.get(ingredient, []) + [food]

# examine the ingredients common to all foods with the same allergens
bad_ingredients = set()
# for each allergen,
for possible_allergen, foods in a_f.items():
    # find the common ingredients between all the foods with the same allergens
    common = reduce(lambda x, y: x.intersection(y), [recipe[food] for food in foods])
    # these are bad ingredients as they cause allergens
    bad_ingredients = bad_ingredients.union(common)
good_ingredients = all_ingredients - bad_ingredients

# compute solution
print(sum([len(i_f[ingredient]) for ingredient in good_ingredients]))
