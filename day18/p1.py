def eval_exp(exp):
    ans = int(exp[0])
    small_stack = []
    for x in exp[1:]:
        if x.isdigit():
            if small_stack[-1] == '+':
                ans += int(x)
            elif small_stack[-1] == '*':
                ans *= int(x)
            small_stack.pop()
        else:
            small_stack.append(x)
    return ans


def evaluate(exp):
    # eval parantheses first
    stack = [x for x in line if x != ' ']
    ans = 0
    current_index = 0
    while '(' in stack:
        # find last opening bracket
        last_open = len(stack) - stack[::-1].index('(') - 1
        # evaluate to first closing bracket
        first_close = last_open + stack[last_open:].index(')')
        # simplify stack
        new = eval_exp(stack[last_open + 1: first_close])
        # update stack
        for _ in range(first_close - last_open + 1):
            stack.pop(last_open)
        stack.insert(last_open, str(new))
    
    return eval_exp(stack)

with open('input.txt', 'r') as f:
    lines = [x.rstrip() for x in f.readlines()]

ans = 0
for line in lines:
    ans += evaluate(line)

print(ans)
