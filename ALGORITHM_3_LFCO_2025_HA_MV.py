def construct_leftmost_derivation(string):
    """
    Constructs and prints a leftmost derivation for a given accepted string,
    along with the rule used in each step.
    """
    if not string:
        print("S -> ε")
        return
    
    steps = ["S"]
    rules = []
    for i in range(len(string) // 2):
        new_step = steps[-1].replace("S", "aSb", 1)
        steps.append(new_step)
        rules.append("S -> aSb")
    
    steps.append(string)  # Final step is the complete string
    rules.append("S -> ε")
    
    print(f"Rule       Sentential forms in a leftmost configuration of x in G for '{string}':")
    print("           S")  # Starting point

    for step, rule in zip(steps[1:], rules):
        print(f"{rule.ljust(10)} {step}")
    print()

if __name__ == "__main__":
    accepted_strings = []
    
    # Read results from pda_results.txt
    with open("pda_results.txt", "r") as pda_output:
        for line in pda_output:
            if "is accepted" in line:
                accepted_strings.append(line.split("'")[1])
    
    # Construct leftmost derivation for accepted strings
    for s in accepted_strings:
        construct_leftmost_derivation(s)