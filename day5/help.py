"""AoC :: Day 5"""
import time
from typing import TextIO
INPUT_FILE = 'input.txt'


def parse(file: TextIO):
    """Parse the plaintext input"""
    page_ordering_rules, update_spec = file.read().split("\n\n")

    # Parse rules into key:val pairs such that the key returns all numbers
    # that must appear after the key as per the inputs
    rules: dict[int, set[int]] = {}
    for line in page_ordering_rules.split("\n"):
        x, y = line.split("|")
        if int(x) in rules:
            rules[int(x)].add(int(y))
        else:
            rules[int(x)] = {int(y)}

    # Return rules dict and the list of updates
    return rules, [[int(n) for n in line.split(",")] for line in update_spec.split("\n") if line]


def valid(rules: dict[int, set[int]], update: list[int]):
    """
    Check if an update is correctly ordered

    We will presume that the rules do not specify a total ordering,
    meaning we cannot simply compare neighbours in an update
    """
    ns = set()
    for n in update:
        if ns & rules.get(n, set()):
            return False
        ns.add(n)
    return True

def part_one(rules: dict[int, set], updates: list[list[int]]):
    """
    Solution to part one
    
    Return the invalid updates since they're relevant to part two
    """
    a1, a2 = 0, 0
    for update in updates:
        k = len(update)//2
        if valid(rules, update):
            a1 += update[k]
        else:
            a2 += median(rules, set(update), k)
    return a1, a2


def median(rules: dict[int, set[int]], update: set[int], k: int) -> int:
    """
    Return the k_th ordered element of this set given the rules
    """
    candidate = update.pop()
    # If this was the last element in update, it must be the k_th element by elimination
    if not update:
        return candidate
    # Else, find the elements that are greater than the candidate using rules
    gt_candidate = update - rules.get(candidate, set())
    # The elements less that the candidate are whatever remains from the update
    lt_candidate = update - gt_candidate

    N = len(lt_candidate)
    # If there are exactly N elements less than the candidate, we've found the median
    if N == k:
        return candidate
    # If there are too many elements less than the candidate, we look for the k_th element of lt_candidate
    if k < N:
        return median(rules, lt_candidate, k)
    # Otherwise, the k_th element is in gt_candidate
    # We subtract N + 1 from k since they're out of consideration
    return median(rules, gt_candidate, k - N - 1)


# run both solutions and print outputs + runtime
def main():
    """The full days solution"""

    # Parse inputs
    print(":: Parsing Inputs ::")
    t0 = -time.time()
    with open(INPUT_FILE, encoding="utf8") as f:
        rules, updates = parse(f)
    t0 += time.time()
    print(f"runtime: {t0: .4f}s")

    # Part One
    print(":: Part One + Two ::")
    t1 = -time.time()
    a1, a2 = part_one(rules, updates)
    t1 += time.time()
    print(f"Part One Answer: {a1}")
    print(f"Part Two Answer: {a2}")
    print(f"runtime: {t1: .4f}s")

    print(f":: total runtime: {t0+t1: .4f}s ::")


if __name__ == "__main__":
    main()