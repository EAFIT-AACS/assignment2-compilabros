import random

def generate_valid_string(length):

    if length == 0:
        return ""
    half = length // 2
    return "a" * half + "b" * half

def generate_invalid_string():

    length = random.randint(1, 5)
    return ''.join(random.choice('ab') for _ in range(length))

if __name__ == "__main__":
    strings = [generate_valid_string(n) for n in [2, 4, 6]] + [generate_invalid_string() for _ in range(2)]
    
    print("Generated strings:")
    for s in strings:
        print(f"String: '{s}'")

    with open("generated_strings.txt", "w") as file:
        for s in strings:
            file.write(s + "\n")
    
    print("Generated strings have been saved to 'generated_strings.txt'")