
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

def part1():
    for size in range(5, len(complete_pool)):
        # Find the first pool where any has Won
        current_pool = complete_pool[0:size]
        state = [board.hasWon(current_pool) for board in boards]
        if any(state):
            for i, s in enumerate(state):
                if s:
                    return boards[i].score(current_pool)
            break

def part2():
    for size in range(5, len(complete_pool)):
        # Find the first pool where they have all Won, therefore,
        #  The pool before is the last board to Win
        current_pool = complete_pool[0:size]
        state = [board.hasWon(current_pool) for board in boards]
        if all(state):
            # Now find that pool hehehehe
            last_losing_pool = complete_pool[0:size-1]
            state = [board.hasWon(last_losing_pool) for board in boards]
            for i, s in enumerate(state):
                # Find the board that hasn't won yet in the last pool
                if not s:
                    return boards[i].score(current_pool)
            break

def getFileLines(filename):
    with open(filename, "r") as file:
        return file.read()

data = getFileLines("Day 4/Day4").split('\n\n')
complete_pool = list(data.pop(0).split(','))
boards = [Board(datum) for datum in data]


print(part1())
print(part2())