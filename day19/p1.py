def flatten_lists(lists):
    return sum(lists, [])

def list_join(lists):
    ans = []
    # multiple options
    linear = True
    for list_index, appending_list in enumerate(lists):      
        if len(appending_list) > 1:
            for option in appending_list:
                # e.g. [[a], [b, c], [d]] ==> [[a], [b], [d]] + [[a], [c], [d]]
                ans += list_join(lists[:list_index] + [[option]] + lists[list_index + 1:])
            linear = False

    # general case (appending_lists linear - single options)
    if linear:
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


memo_rules = {}
def translate_rule(rules, rule_number):
    # memoization
    if rule_number in memo_rules:
        return memo_rules[rule_number]
    rule = rules[rule_number]
    # "a" or "b"
    if rule.startswith('"'):
        memo_rules[rule_number] = [rule[1]] # ['a'] or ['b']
    # pipe
    elif '|' in rule:
        memo_rules[rule_number] = flatten_lists([list_join([translate_rule(rules, choice) for choice in option.split(' ')]) for option in rule.split(' | ')])
    # sequence
    else:
        memo_rules[rule_number] = list_join([translate_rule(rules, choice) for choice in rule.split(' ')])
    return memo_rules[rule_number]

if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]
    rule_lines = [x.split(': ') for x in lines[:129]]
    messages = lines[130:]

    # dict of rules
    rules = {line[0]: line[1] for line in rule_lines}
    # translate rule 0
    valid = set(translate_rule(rules, '0'))

    # number of valid messages
    print(len(valid.intersection(set(messages))))
