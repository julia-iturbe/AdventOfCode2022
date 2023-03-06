lines = [line.strip() for line in open("inputs/day4.txt", "r")]

pairs_contained = 0
pairs_overlap = 0  # part 2
for line in lines:
    tmp1, tmp2 = line.split(",")
    e1s, e1e = tmp1.split("-")
    e2s, e2e = tmp2.split("-")
    e1 = range(int(e1s), int(e1e) + 1)
    e2 = range(int(e2s), int(e2e) + 1)
    if set(e1) <= set(e2) or set(e2) <= set(e1):
        pairs_contained += 1
    if len(list(set(e1) & set(e2))) > 0:
        pairs_overlap += 1
print("Pairs contained: " + str(pairs_contained))
print("Pairs with overlap: " + str(pairs_overlap))
