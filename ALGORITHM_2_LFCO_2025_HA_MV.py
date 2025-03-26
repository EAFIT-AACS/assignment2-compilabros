def pda_recognizer(input_string):

    stack = []
    for char in input_string:
        if char == 'a':
            stack.append('a')
        elif char == 'b':
            if stack:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

if __name__ == "__main__":
    with open("generated_strings.txt", "r") as file:
        test_strings = [line.strip() for line in file]
    
    for s in test_strings:
        result = "accepted" if pda_recognizer(s) else "rejected"
        print(f"The string '{s}' is {result} by the PDA")