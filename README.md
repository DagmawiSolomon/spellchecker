# SpellChecker

A Python-based spellchecker that utilizes the [**Wagner-Fischer algorithm**](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm) to calculate the [**Levenshtein distance**](https://en.wikipedia.org/wiki/Levenshtein_distance), ensuring accurate and efficient spell correction.

## Features

- **Levenshtein Distance Calculation**  
  Implements the [**Wagner-Fischer algorithm**](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm) to determine the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one word into another.

- **Basic Spell Checking**  
  Compares input words against a dictionary to suggest the closest matches.

- **Modular Design**  
  The code is structured for easy readability and future extensions.

---

## Planned Features

### 1. **BK-Tree Integration**  
   - Optimize dictionary storage and retrieval for faster spell-checking in future versions.

### 2. **Web Interface**
   - **Visualization Tool**: Displays the step-by-step process of the Wagner-Fischer algorithm.
   - **Real-Time Spellchecking**: Adds live spell correction for web users.

---

## How It Works

1. **Input Handling**  
   Accepts a word or text file as input.
   
2. **Dictionary Lookup**  
   - Checks the dictionary for the closest matches to the input using Levenshtein distance.
   
3. **Spell Checking**  
   - Suggests corrections for misspelled words based on computed distances.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DagmawiSolomon/spellchecker
   cd spellchecker
   ```
---

## Usage

### Spell Check a Word
```bash
python cli.py --word <word>
```
### Spell Check a file
```bash
python cli.py --file <filepath>
```
---

## Why Wagner-Fischer?

- **Efficiency**: A dynamic programming approach to calculate Levenshtein distance accurately.
- **Accuracy**: Identifies the best possible corrections by computing exact distances between words.



## Contribution

I welcome contributions! Here's how you can help:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---




