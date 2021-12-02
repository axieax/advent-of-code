def eval_exp(exp):
    ''' evaluates a simple expression without parantheses '''
    # normal computation - keeping track of previous operation
    ans = int(exp[0])
    op_stack = []
    for x in exp[1:]:
        if x.isdigit():
            if op_stack[-1] == '+':
                ans += int(x)
            elif op_stack[-1] == '*':
                ans *= int(x)
            op_stack.pop()
        else:
            op_stack.append(x)
    
    return ans


def evaluate(exp):
    ''' evaluates a complicated expression (list) '''
    # eval parantheses first
    ans = 0
    current_index = 0
    # eval parantheses first
    while '(' in exp:
        # find last opening bracket (first occurence in reversed exp)
        last_open = len(exp) - exp[::-1].index('(') - 1
        # evaluate to first closing bracket
        first_close = last_open + exp[last_open:].index(')')
        # simplify exp
        new = eval_exp(exp[last_open + 1: first_close])
        # update exp by replacing expression in parantheses
        for _ in range(first_close - last_open + 1):
            exp.pop(last_open)
        exp.insert(last_open, str(new))
    
    return eval_exp(exp)


if __name__ == '__main__':
    # extract input from file
    with open('input.txt', 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]

    # evaluate input expressions
    ans = 0
    for line in lines:
        ans += evaluate([x for x in line if x != ' '])
    print(ans)
