

with open("input.txt", "rb") as fd:
    elves = []
    elf_ctr = 0
    while 1:
        line = fd.readline()
        if line == b"\n":
            elf_ctr += 1
            continue
        elif line == b"":
            break
        line = line.strip(b"\n")
        line = int(line.decode())
        if len(elves) == elf_ctr:
            elves.append(line)
        else:
            elves[elf_ctr] += line
    print(f"The elf that had the most calories had {max(elves)} calories.")
    top3 = 0
    for i in range(3):
        top3 += max(elves)
        elves.remove(max(elves))
    print(f"The sum of the calories of the top 3 elves was {top3}.")



