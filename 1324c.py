import sys

def get_input():
    input = []

    for line in sys.stdin:
        input.append(line.strip())

    return input

def frog_jumps(input):
    for i in range(1, len(input)):
        string = input[i]

        position = [0]
        result = 0

        for j, letter in enumerate(string):
            if letter == "R":
                position.append(j + 1)

        position.append(len(string) + 1)

        for j in range(len(position) - 1):
            result = max(result, position[j + 1] - position[j])

        print(result)

input = get_input()
frog_jumps(input)
