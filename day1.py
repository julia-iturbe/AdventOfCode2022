
with open('inputs/day1.txt') as f:
    lines = f.readlines()

elves = lines.count('\n') + 1

elfcals = [0]*(elves)
elf_count = 0

for i in range(len(lines)):
    if lines[i]=='\n':
        elf_count+=1 # New elf
    else:
        # Adding to the current elf
        elfcals[elf_count] += int(lines[i].strip())
#print(elfcals)
print('Highest calories: ' +  str(max(elfcals)))

# part2
elfcals.sort()
top3 = elfcals[-1] + elfcals[-2] + elfcals[-3]
print('Calories from top 3 elves: ' + str(top3))