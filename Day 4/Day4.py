def getFileLines(filename):
    with open(filename, "r") as file:
        return file.read()

data = getFileLines("Day 4/Day4")

# data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""


data = data.split('\n\n')
choose = list(data.pop(0).split(','))

class Board:
    def __init__(self, data: str) -> None:
        rawboard = data.split()
        self.rows = [rawboard[x:x+5] for x in range(0, 25, 5)]
        self.cols = list(zip(*self.rows))
        self.list = rawboard

        self.pool = []

    def hasWon(self, pool: list =[]):
        if pool == []:
            pool = self.pool

        rows = [all([x in pool for x in row]) for row in self.rows]
        cols = [all([x in pool for x in row]) for row in self.cols]
        return any(rows + cols)

    def score(self, pool:list =[]):
        if pool == []:
            pool = self.pool
            
        sum = 0
        for item in filter(lambda x: x not in pool, self.list):
            sum += int(item)
        last_picked = int(pool[-1])
        return sum * last_picked

    def usePool(self, pool):
        self.pool = pool

boards = [Board(datum) for datum in data]

def part1():
    for size in range(5, len(choose)):
        # Find the first pool where any has Won
        current_pool = choose[0:size]
        state = [board.hasWon(current_pool) for board in boards]
        if any(state):
            for i, s in enumerate(state):
                if s:
                    return boards[i].score(current_pool)
            break

def part2():
    for size in range(5, len(choose)):
        # Find the first pool where they have all Won, therefore,
        #  The pool before is the last board to Win
        current_pool = choose[0:size]
        state = [board.hasWon(current_pool) for board in boards]
        if all(state):
            # Now find that pool hehehehe
            last_losing_pool = choose[0:size-1]
            state = [board.hasWon(last_losing_pool) for board in boards]
            for i, s in enumerate(state):
                # Find the board that hasn't won yet in the last pool
                if not s:
                    return boards[i].score(current_pool)
            break

print(part1())
print(part2())