import random
import os

def generate_valid_string(length):
    if length == 0:
        return ""
    half = length // 2
    return "a" * half + "b" * half

def generate_invalid_string():
    length = random.randint(1, 5)
    while True:
        s = ''.join(random.choice('ab') for _ in range(length))
        if s.count('a') != s.count('b') or 'ba' in s:
            return s

def run():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(BASE_DIR, "generated_strings.txt")

    accepted = [generate_valid_string(n) for n in [2, 4, 6]]
    rejected = [generate_invalid_string() for _ in range(2)]
    all_strings = accepted + rejected

    # Guardar en archivo
    with open(output_path, "w") as file:
        for s in all_strings:
            file.write(s + "\n")

    return {
        'accepted': accepted,
        'rejected': rejected
    }