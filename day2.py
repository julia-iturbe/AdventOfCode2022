# Part 1
# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# scores: Rock 1, Paper 2, Scissors 3
# scores: Win 6, Draw 3, Lose 0

# Rules wrt second player
rules = ["AXD3", "AYW6", "AZL0", "BXL0", "BYD3", "BZW6", "CXW6", "CYL0", "CZD3"]
score_values = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

with open("inputs/day2.txt") as f:
    rounds = f.readlines()

total_score = 0
for round in rounds:
    p1, p2 = round.split()
    score = 0
    for rule in rules:
        if rule[0] == p1 and rule[1] == p2:
            score += int(rule[3])
            score += score_values[p2]
    total_score += score

print("Total score: " + str(total_score))

# Part 2
# X lose, Y draw, and Z win

# new definitions
new_defs = {"X": "L", "Y": "D", "Z": "W"}

total_score = 0
for round in rounds:
    p1, r = round.split()
    score = 0
    for rule in rules:
        if rule[0] == p1 and rule[2] == new_defs[r]:
            score += int(rule[3])
            score += score_values[rule[1]]
    total_score += score

print("Total score: " + str(total_score))
