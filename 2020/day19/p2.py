from p1 import flatten_lists, list_join, translate_rule

# extract input from file
with open('input.txt', 'r') as f:
    lines, messages = [x.split('\n') for x in (f.read() + '\n').split('\n\n')]
rule_lines = [x.split(': ') for x in lines]
messages = [x for x in messages if x]
max_message_length = max([len(msg) for msg in messages])

# dict of rules
rules = {line[0]: line[1] for line in rule_lines}
# rule 0: 8 11
# rule 8: 42 | 42 8
# rule 11: 42 31 | 42 11 31

# insights from https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggqxm8m?utm_source=share&utm_medium=web2x&context=3
# note: all blocks have the same length (component_length)
rule_42 = translate_rule(rules, '42')
rule_31 = translate_rule(rules, '31')
component_length = len(rule_42[0])

valid = 0
for message in messages:
    # message should be divisible by the component length
    if len(message) % component_length != 0:
        continue
    # extract component blocks
    components = [message[component_length * i: component_length * (i + 1)] for i in range(0, len(message)//8)]
    # examine components up to the last one
    satisfy_31 = 0
    satisfy_42 = 0
    bad = False
    for index, component in enumerate(components[:-1]):
        found = False
        if component in rule_31:
            # if a block satisfies rule 31, the next block cannot satisfy rule 42 (31 is always at the end)
            if components[index + 1] in rule_42:
                bad = True
                break
            found = True
            satisfy_31 += 1
        if component in rule_42:
            found = True
            satisfy_42 += 1
        if not found:
            # each component has to belong to either rule 31 or rule 42
            bad = True
            break
    # update count for last component (has to satisfy rule 31 as it is at the end)
    satisfy_31 += components[-1] in rule_31
    # num components satisfying rule 42 should be at least one more than num components satisfying rule 31
    if bad or satisfy_42 <= satisfy_31 or (components[-1] not in rule_31):
        continue
    valid += 1

print(valid)
