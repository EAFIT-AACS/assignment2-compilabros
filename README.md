# Assingment 2

## Authors
- **Moises Arturo Vergara Garces**
- **Hever Andre Alfonso Jimenez**

## System and Tools Used
- **Operating System:** Linux Mint 22.1
- **Programming Language:** Python 3.12.3
- **References:** Lectures 19, 20, 23, and 24 from *Automata and Computability* by Dexter C. Kozen

## Project Overview
This project implements three algorithms related to Context-Free Grammars (CFG) and Pushdown Automata (PDA). The grammar used is:

G: S -> aSb | ε

The implementation consists of three scripts:

1. **ALGORITHM_1_LFCO_2025_HA_MV.py**: Generates strings and saves them in a generated_strings.txt file.
2. **ALGORITHM_2_LFCO_2025_HA_MV.py**: Implements a PDA that accepts or rejects strings in generated_strings.txt file and logs the output in a pda_resulsts_ file.
3. **ALGORITHM_3_LFCO_2025_HA_MV.py**: Constructs the leftmost derivation for accepted strings in pda_results.txt.

## Instructions for Running the Implementations

### 1. Running **Algorithm 1**
This script generates a set of strings (both valid and invalid) and saves them to `generated_strings.txt`.

#### Steps:
```bash
python3 ALGORITHM_1_LFCO_2025_HA_MV.py
```

#### Expected Output:
```
Generated strings:
String: 'aabb'
String: 'aaabbb'
String: 'abab'
String: 'aaaabbbb'
String: 'aabbb'
Generated strings have been saved to 'generated_strings.txt'
```

### 2. Running **Algorithm 2**
This script reads the generated strings from `generated_strings.txt`, processes them using a PDA, and determines if they are accepted. The results are saved to `pda_results.txt`

#### Steps:
```bash
python3 ALGORITHM_2_LFCO_2025_HA_MV.py
```

#### Expected Output:
```
The string 'aabb' is accepted by the PDA
The string 'aaabbb' is accepted by the PDA
The string 'abab' is rejected by the PDA
The string 'aaaabbbb' is accepted by the PDA
The string 'aabbb' is rejected by the PDA
```

### 3. Running **Algorithm 3**
This script reads strings from `pda_results.txt` and generates their leftmost derivation.

#### Steps:
```bash
python3 ALGORITHM_3_LFCO_2025_HA_MV.py
```

#### Expected Output:
```
Rule       Sentential forms in a leftmost configuration of x in G for 'aabb':
           S
S -> aSb   aSb
S -> aSb   aaSbb
S -> ε     aabb
```

## Notes
- Ensure that **Algorithm 1** runs first to generate the necessary input file.
- **Algorithm 2** must be executed before **Algorithm 3** to identify accepted strings and store them in `pda_results.txt`.
- If any script does not run, check that Python 3.12.3 is installed using:
  ```bash
  python3 --version
  ```

