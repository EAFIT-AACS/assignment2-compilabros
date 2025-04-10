import os

def construct_leftmost_derivation(string):
    if not string:
        return "S → ε"

    steps = ["S"]
    rules = []
    for _ in range(len(string) // 2):
        new_step = steps[-1].replace("S", "aSb", 1)
        steps.append(new_step)
        rules.append("S → aSb")

    steps.append(string)
    rules.append("S → ε")

    derivation = ["S"]
    for step, rule in zip(steps[1:], rules):
        derivation.append(f"{rule}     {step}")

    return "\n".join(derivation)

def run():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    results_path = os.path.join(BASE_DIR, "pda_results.txt")

    if not os.path.exists(results_path):
        return {'Error': 'Archivo pda_results.txt no encontrado. Ejecutá el Algoritmo 2 primero.'}

    accepted_strings = []

    with open(results_path, "r") as file:
        for line in file:
            if "is accepted" in line:
                # Extraer la cadena entre comillas
                string = line.split("'")[1]
                accepted_strings.append(string)

    print("Accepted strings:", accepted_strings)  # ✅ ahora sí, ya existe la variable

    derivations = {}
    for s in accepted_strings:
        derivations[s] = construct_leftmost_derivation(s)

    return derivations