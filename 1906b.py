import sys
 
def get_input():
    input = []
 
    for line in sys.stdin:
        input.append(line.strip())
 
    return input

def yabk(input):
    test_cases = int(input[0])

    lower_chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(1, test_cases + 1):
        case_dict = {
            "upper": [],
            "lower": [],
        }

        string = [x for x in input[i]]

        for j, char in enumerate(string):
            if char == "b":
                string[j] = ""

                if case_dict["lower"]:
                    string[case_dict["lower"].pop()] = ""


            elif char == "B":
                string[j] = ""

                if case_dict["upper"]:
                    string[case_dict["upper"].pop()] = ""

            else:
                if char in upper_chars:
                    case_dict["upper"].append(j)

                if char in lower_chars:
                    case_dict["lower"].append(j)

        print("".join(string))

input = get_input()
yabk(input)
