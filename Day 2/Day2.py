# horizontal = 0
# vertical = 0
# aim = 0

# hva = [0,0,0]

# commands = {
#     "forward" : lambda value, hva=hva: [(hva[0] + value), (hva[1] + value * hva[2]), hva[2]],
#     "up" : lambda value, hva=hva: [hva[0], hva[1], (hva[2] - value)],
#     "down" : lambda value, hva=hva: [hva[0], hva[1], (hva[2] + value)]
# }

# with open("Day 2/Day2", 'r') as file:
#     for line in file.readlines():
#         l,r = line.split(" ");
#         hva = commands[l](int(r), hva)

# horizontal, vertical, aim = hva

# with open("Day 2/Day2", 'r') as file:
#     for line in file.readlines():
#         command, value = line.split(" ")
#         value = int(value)

#         if command == "forward":
#             horizontal += value
#             vertical += value * aim

#         if command == "up":
#             aim -= value
#         if command == "down":
#             aim += value



# print(horizontal * aim) # Part 1
# print(horizontal * vertical) # Part 2

import operator

class Submarine:

    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.aim = 0

    def part1(self):
        return self.horizontal * self.aim

    def part2(self):
        return self.horizontal * self.vertical

    def forward(self, value: int):
        self.horizontal += value
        self.vertical += value * self.aim

    def up(self, value: int):
        self.aim -= value
    def down(self, value: int):
        self.aim += value

sub = Submarine()
with open("Day 2/Day2", 'r') as file:
    [operator.methodcaller(l,int(r))(sub) for l,r in [line.split(" ") for line in file.readlines()]]

print(sub.part1())
print(sub.part2())