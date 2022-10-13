nums = list(map(int, input()))

num2syms = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}


def get_combinations(nums, string):
    if len(nums) == 0:
        return [string]

    syms = num2syms[nums[0]]
    combs = []
    for sym in syms:
        combs += get_combinations(nums[1:], string + sym)
    return combs

print(*get_combinations(nums, ""))
