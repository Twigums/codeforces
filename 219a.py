import sys

def get_input():
    input = []
    
    for line in sys.stdin:
        input.append(line.strip())
        
    return input
    
def k_string(input):
    k = int(input[0])
    string = input[1]
    
    letter_dict = {}
    pattern = ""
    result = ""
    
    for letter in string:
        if letter in letter_dict:
            letter_dict[letter] += 1
            
        else:
            letter_dict[letter] = 1
    
    for letter in letter_dict:
        if letter_dict[letter] % k != 0:
            return -1

        for i in range(int(letter_dict[letter] / k)):
            pattern += letter
            
    for i in range(k):
        result += pattern
            
    return result
    
input = get_input()
print(k_string(input))
