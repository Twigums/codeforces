import sys
 
def get_input():
    input = []
 
    for line in sys.stdin:
        input.append(line.strip())
 
    return input

def swap_and_delete(input):
    test_cases = int(input[0])

    for i in range(1, test_cases + 1):
        s = input[i]
        count = 0

        val_dict = {
            "0": 0,
            "1": 0,
        }

        for val in s:
            val_dict[val] += 1

        for val in s:
            if val == "0" and val_dict["1"] != 0:
                val_dict["1"] -= 1
                count += 1

            elif val == "1" and val_dict["0"] != 0:
                val_dict["0"] -= 1
                count += 1

            else:
                break

        print(len(s) - count)

input = get_input()
swap_and_delete(input)
