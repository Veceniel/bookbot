#Here's my main.py
import sys
from stats import word_count
from stats import letter_count
from stats import sort_chars

def get_book_text(file):
    return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        text = get_book_text(f)
        letters = letter_count(text)
        sorted = sort_chars(letters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(text)} total words")
        print("--------- Character Count -------")
        for set in sorted:
            if set["char"].isalpha():
                print(f"{set["char"]}: {set["num"]}")
            else:
                pass
        print("============= END ===============")

main()
