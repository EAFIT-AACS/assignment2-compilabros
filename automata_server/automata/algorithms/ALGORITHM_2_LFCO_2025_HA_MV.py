import os

def pda_recognizer(input_string):
    stack = []
    history = []
    for i, char in enumerate(input_string):
        if char == 'a':
            stack.append('a')
            history.append(f"Step {i+1}: Read 'a', push → {stack}")
        elif char == 'b':
            if stack:
                stack.pop()
                history.append(f"Step {i+1}: Read 'b', pop → {stack}")
            else:
                history.append(f"Step {i+1}: Read 'b', but stack empty → rejected")
                return False, history

    if len(stack) == 0:
        history.append("Final: Stack empty → accepted")
        return True, history
    else:
        history.append("Final: Stack not empty → rejected")
        return False, history

def run():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(BASE_DIR, "generated_strings.txt")
    output_path = os.path.join(BASE_DIR, "pda_results.txt")

    if not os.path.exists(input_path):
        return [{'string': 'Archivo no encontrado', 'accepted': False, 'history': ['El archivo no existe. Ejecutá el Algoritmo 1 primero.']}]

    with open(input_path, "r") as file:
        test_strings = [line.strip() for line in file]

    results = []

    with open(output_path, "w") as result_file:
        for s in test_strings:
            accepted, history = pda_recognizer(s)
            result_file.write(f"The string '{s}' is {'accepted' if accepted else 'rejected'} by the PDA\n")
            results.append({'string': s, 'accepted': accepted, 'history': history})

    return results