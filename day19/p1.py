def flatten_lists(lists):
    return sum(lists, [])

def list_join(lists):
    ans = []
    list_of_lists_present = False
    list_of_strings_present = False
    # e.g. lists = [['a'],      [['ab'], ['ba']]]
    for index, appending_list in enumerate(lists):
        # list of lists
        if isinstance(appending_list[0], list):
            for sub_list in appending_list:
                ans.append(list_join(lists[:index] + [sub_list] + lists[index + 1:]))
                list_of_lists_present = True
        # list with multiple options
        elif len(appending_list) > 1:
            for string in appending_list:
                ans.append(list_join(lists[:index] + [[string]] + lists[index + 1:]))
                list_of_strings_present = True
    if list_of_lists_present:
        return flatten_lists(ans)
    elif list_of_strings_present:
        return ans

    ans = ['']
    for appending_list in lists:
        # resize
        list_size = len(appending_list)
        ans *= list_size
        for index, element in enumerate(appending_list):
            # range(index * list_size, (index + 1) * list_size)
            for i in range(index * list_size, (index + 1) * list_size):
                ans[i] += element
    return ans


def translate_rule(rule_number):
    global rules
    rule = rules[rule_number]
    if rule.startswith('"'):
        return [rule[1]]
    # pipe
    elif '|' in rule:
        return [list_join([translate_rule(choice) for choice in option.split(' ')]) for option in rule.split(' | ')]
    else:
        return [list_join([translate_rule(choice) for choice in rule.split(' ')])]


# extract input from file
with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]
rule_lines = [x.split(': ') for x in lines[:129]]
messages = lines[130:]

# dict of rules
rules = {line[0]: line[1] for line in rule_lines}
# translate dict
valid = flatten_lists(translate_rule('0'))
while isinstance(ans[0], list):
    valid = flatten_lists(valid)
valid = list(set(valid))

print(valid)
# print(len([x for x in messages if x in valid]))

