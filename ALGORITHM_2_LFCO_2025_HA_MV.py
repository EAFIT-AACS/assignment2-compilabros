def pda_recognizer(input_string):
    """
    Pushdown Automaton (PDA) to recognize strings from the grammar G: S -> aSb | ε.
    """
    stack = []
    for char in input_string:
        if char == 'a':
            stack.append('a')  # Push 'a' onto the stack
        elif char == 'b':
            if stack:
                stack.pop()  # Pop 'a' if available
            else:
                return False  # More 'b's than 'a's -> Invalid string
    
    return len(stack) == 0  # Stack should be empty if valid

if __name__ == "__main__":
    with open("generated_strings.txt", "r") as file:
        test_strings = [line.strip() for line in file]
    
    with open("pda_results.txt", "w") as result_file:
        for s in test_strings:
            result = "accepted" if pda_recognizer(s) else "rejected"
            output = f"The string '{s}' is {result} by the PDA\n"
            print(output.strip())
            result_file.write(output)