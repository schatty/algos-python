n = int(input())

def get_brackets_seq(seq, open_left, closed_left):
    if closed_left == 0:
        return seq

    if open_left == 0:
        # print("closing case")
        return get_brackets_seq(seq + ")", open_left, closed_left - 1)
    
    # Can open two cases, one with closing bracket, another with opening
    if closed_left > open_left:
        branch_1 = get_brackets_seq(seq + "(", open_left - 1, closed_left)
        branch_2 = get_brackets_seq(seq + ")", open_left, closed_left - 1)
        if isinstance(branch_1, list) and isinstance(branch_2, list):
            return [*branch_1, *branch_2]
        elif isinstance(branch_1, list):
            return [*branch_1, branch_2]
        elif isinstance(branch_2, list):
            return [branch_1, *branch_2]
        else:
            return [branch_1, branch_2]
    # If closed_left == open_left than we can afford only opening
    else:
        return get_brackets_seq(seq + "(", open_left - 1, closed_left)

seq = get_brackets_seq("(", n-1, n)
if isinstance(seq, list):
    print(*seq, sep='\n')
else:
    print(seq)
