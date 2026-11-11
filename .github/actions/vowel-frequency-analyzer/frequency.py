import sys
from collections import Counter


def count_vowels(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' could not be found.")
        sys.exit(1)

    vowels = "aeiou"
    counts = Counter(character for character in text if character in vowels)

    print("Vowel Frequency Analysis")
    print("------------------------")
    print(f"File analysed: {file_path}")

    for vowel in vowels:
        print(f"{vowel}: {counts[vowel]}")

    print("------------------------")
    print("Analysis completed successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frequency.py <text-file>")
        sys.exit(1)

    count_vowels(sys.argv[1])
