import os

def construct_leftmost_derivation(string):

    if not string:
        print("S -> ε")
        return
    
    steps = ["S"]
    rules = []
    for i in range(len(string) // 2):
        new_step = steps[-1].replace("S", "aSb", 1)
        steps.append(new_step)
        rules.append("S -> aSb")
    
    steps.append(string)
    rules.append("S -> ε")
    
    print(f"Rule       Sentential forms in a leftmost configuration of x in G for '{string}':")
    print("           S")

    for step, rule in zip(steps[1:], rules):
        print(f"{rule.ljust(10)} {step}")
    print()

if __name__ == "__main__":
    accepted_strings = []
    

    with os.popen("python3 ALGORITHM_2_LFCO_2025_HA_MV.py") as pda_output:
        for line in pda_output:
            if "is accepted" in line:
                accepted_strings.append(line.split("'")[1])
    

    for s in accepted_strings:
        construct_leftmost_derivation(s)