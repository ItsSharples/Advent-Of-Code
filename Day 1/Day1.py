
count = 0
index = 0;
window = []
with open("Day 1/Day1", 'r') as file:
    for line in file.readlines():
        value = int(line)

        window.append(value)

        last = sum(window[-5:-2])
        curr = sum(window[-4:-1])

        if(index < -1):
            print(window[-4:-1])
            print(window[-3:])

        if last < curr:
            count += 1

        index+=1

print(count)
