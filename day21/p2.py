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
# map from food to possible allergens
f_a = {}

all_allergens = set()
all_ingredients = set()
for food, line in enumerate(lines):
    # extract data
    ingredients, allergens = line[:-1].split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.split(', ')
    all_ingredients = all_ingredients.union(set(ingredients))
    all_allergens = all_allergens.union(set(allergens))
    # mapping from possible allergen to foods
    for allergen in allergens:
        a_f[allergen] = a_f.get(allergen, []) + [food]
    # mapping from food to ingredients
    recipe[food] = set(ingredients)
    # mapping from ingredient to foods
    for ingredient in ingredients:
        i_f[ingredient] = i_f.get(ingredient, []) + [food]
    # mapping from food to possible allergens
    f_a[food] = allergens

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
# a_i = a_f, f_i
a_i = {}
for allergen in all_allergens:
    foods = a_f[allergen]
    a_i[allergen] = set([ingredient for ingredient in recipe[food] for food in foods if ingredient in bad_ingredients])
    print(a_i[allergen])
    # remove good ingredients

print(a_i)
print(good_ingredients)



# print(bad_ingredients)
# print(recipe)
# print(i_f)
# print(a_f)


# # for each ingredient, for each possible allergen
# # a definite allergen is where the allergen is present for all foods using the ingredient
# for ingredient, foods in i_f.items():
#     # ignore good ingredients
#     if ingredient in good_ingredients:
#         continue
#     print(ingredient, foods)
#     # find possible allergens
#     possible_allergens = set()
#     for food in foods:
#         possible_allergens = possible_allergens.union(set(f_a[food]))
#     print(possible_allergens)
#     # for all foods using ingredient, make sure allergen is present
#     for allergen in possible_allergens:
#         if all([allergen in f_a[food] for food in foods]):
#             print(allergen)

