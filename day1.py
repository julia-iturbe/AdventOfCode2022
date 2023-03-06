with open("inputs/day1.txt") as f:
    lines = f.readlines()

elves = lines.count("\n") + 1

elfcals = [0] * (elves)
elf_count = 0

for line in lines:
    if line == "\n":
        elf_count += 1  # New elf
    else:
        # Adding to the current elf
        elfcals[elf_count] += int(line.strip())
# print(elfcals)
print("Highest calories: " + str(max(elfcals)))

# part2
elfcals.sort()
top3 = sum(elfcals[-3:])
print("Calories from top 3 elves: " + str(top3))
