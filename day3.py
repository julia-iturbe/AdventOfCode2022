import string

lines = [line.strip() for line in open('inputs/day3.txt', 'r')]

def priority(test):
    priority = string.ascii_lowercase.index(test.lower()) + 1
    if test.isupper():
        priority += 26
    return priority
    
total_priority = 0
for line in lines:
    halfway = int(len(line)/2)
    part1 = line[:halfway]
    part2 = line[halfway:]
    rept = list(set(part1) & set(part2))
    if len(rept) != 1:
        print("Something funny going on")
    total_priority += priority(rept[0])
print('Total priority: '+ str(total_priority))

# Part 2

total_priority = 0
for i in range(0, len(lines), 3):
    rept = list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))
    if len(rept) != 1:
        print("Something funny going on")
    total_priority+=priority(rept[0])
print('Total priority: ' + str(total_priority))
