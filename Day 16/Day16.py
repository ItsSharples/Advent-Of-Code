from math import prod
from enum import IntEnum, unique
from typing import Iterable

from collections import deque

@unique
class Stages(IntEnum):
    PACKET = 0, # 6 Bits Version and ID
    TYPE = 2, # 1 Bit Type
    COUNT = 3, # 11 Bits, denoting number of Sub Packets
    LENGTH = 4, # 15 Bits, denoting length of Subpacket

    LITERAL = 1

@unique
class Operator(IntEnum):
    SUM = 0,
    PDT = 1,
    MIN = 2,
    MAX = 3,
    GRT = 5,
    LST = 6,
    EQL = 7,
    LTL = 4

    def __repr__(self) -> str:
        return super().name

    def do(self, numbers: Iterable ):
        match(self):
            case(Operator.SUM): return sum(numbers)
            case(Operator.PDT): return prod(numbers)
            case(Operator.MIN): return min(numbers)
            case(Operator.MAX): return max(numbers)
            case(Operator.GRT): return 1 if numbers[0] > numbers[1] else 0
            case(Operator.LST): return 1 if numbers[0] < numbers[1] else 0
            case(Operator.EQL): return 1 if numbers[0] == numbers[1] else 0
            case(_): return numbers


def readPacket(data: list[str]):
    length = len(data)
    iterator = 0
    stage: Stages = Stages.PACKET
    output = []
    while iterator < length:
        match stage:
            case(Stages.PACKET):
                if iterator + 6 > length: break
                read = data[iterator: iterator+6]
                iterator += 6
                Version, ID = int(read[:3],2), Operator(int(read[3:],2))

                if ID.value == 4: stage = Stages.LITERAL
                else:
                    output.append(ID)
                    stage = Stages.TYPE

            case(Stages.LITERAL):
                values = ""

                read = data[iterator: iterator+5]
                iterator += 5
                values += read[1:]
                while read and read[0] != '0':
                    read = data[iterator: iterator+5]
                    iterator += 5
                    values += read[1:]

                number = int("".join(values), 2)
                output.append(number)
                break

            case(Stages.TYPE):
                read = data[iterator]
                iterator += 1

                if read == "0":
                    stage = Stages.LENGTH
                else:
                    stage = Stages.COUNT

            case(Stages.COUNT):
                # Read 11 Bits to find the number of subpackets this contains
                number = int(data[iterator: iterator + 11], 2)
                iterator += 11
                
                packetSize = length - iterator
                # print(f"Count: {number}, Packet Size: {packetSize}")
                values = []
                for _ in range(number):
                    answer, usedIterator = readPacket(data[iterator: iterator+packetSize])
                    iterator += usedIterator
                    if answer: output.append(answer)
                
                break

            case(Stages.LENGTH):
                # Read 15 Bits to find the length of the subpacket
                packetSize = int(data[iterator: iterator + 15], 2)
                iterator += 15
                goneThrough = 0
                values = []
                while goneThrough < packetSize:
                    answer, usedIterator = readPacket(data[iterator: iterator+packetSize])
                    iterator += usedIterator
                    goneThrough += usedIterator
                    if answer: output.append(answer)
                break

    return output, iterator


with open("Day 16/Day16", "rb") as file:
    fileStr = file.read()
    # For some reason it wants to keep the 0b, sooooo
    fileData = bin(int(fileStr, 16))[2:]
    # But then we need to replace the missing zeros that were cut off
    missingLeading = len(fileStr) * 4
    filePadded = fileData.zfill(missingLeading)

instructions, _ = readPacket(filePadded)

def compute(instructions):
    if len(instructions) == 1: return instructions[0]
    return instructions[0].do([compute(item) for item in instructions[1:]])

print(compute(instructions))