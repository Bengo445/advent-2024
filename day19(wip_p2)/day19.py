_input = open("input.txt", "r").read().split("\n\n")

result = 0
towels = set(towel.strip() for towel in _input[0].split(","))

def solve_design(i, design, lvl, memo):
    if i in memo:
        return memo[i]
    
    design_len = len(design)
    max_len = max(len(towel) for towel in towels)
    extra_len = 1
    while extra_len <= min(max_len, design_len - i):
        checking_part = design[i:i+extra_len]
        if checking_part in towels:
            if i + extra_len == design_len:
                memo[i] = 1
                return 1
            if solve_design(i + extra_len, design, lvl + 1, memo) == 1:
                memo[i] = 1
                return 1
        extra_len += 1
    
    memo[i] = 0
    return 0

for design in _input[1].split("\n"):
    design = design.strip()
    print(f"design: '{design}'")
    memo = {}
    result += solve_design(0, design, 0, memo)

print(result)
