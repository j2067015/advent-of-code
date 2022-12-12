with open("5-Supply-Stacks/input.txt", "r") as file:
    fd = file.read().split("\n")
    fd.pop()

buckets = []
for i in range(8):
    line = fd.pop(0)
    line = [line[x] for x, _ in enumerate(line) if (x % 4) - 1 == 0]
    buckets.append(line)

buckets = list(zip(*buckets))
buckets = ["".join(x).strip() for x in buckets]
buckets = [list(x) for x in buckets]
fd.pop(0)
fd.pop(0)

def part_one():
    for ctr, line in enumerate(fd):
        
        line = line.replace("move ", "").replace("from ", "").replace("to ", "")
        line = line.split(" ")
        line = [int(x) for x in line]
        amount, sender, destination = line[:]
        sender, destination = sender - 1, destination - 1

        moving = buckets[sender][0:amount]
        for i in range(amount):
            buckets[sender].pop(0)

        
        buckets[destination] = moving[::-1] + buckets[destination]
    
    for b in buckets:
        print(b[0], end="")

def part_two():
    for ctr, line in enumerate(fd):
        
        line = line.replace("move ", "").replace("from ", "").replace("to ", "")
        line = line.split(" ")
        line = [int(x) for x in line]
        amount, sender, destination = line[:]
        sender, destination = sender - 1, destination - 1

        moving = buckets[sender][0:amount]
        for i in range(amount):
            buckets[sender].pop(0)

        
        buckets[destination] = moving[:] + buckets[destination]
    
    for b in buckets:
        print(b[0], end="")

part_two()