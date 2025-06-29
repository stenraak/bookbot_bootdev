import sys
from stats import (
    number_of_words_in_string,
    get_character_count,
    sort_list_of_dictionaries
)

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        content = f.read()
        return content
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    nr_of_words = number_of_words_in_string(get_book_text(sys.argv[1]))
    count_chars = get_character_count(get_book_text(sys.argv[1]))    
    char_counts = sort_list_of_dictionaries(count_chars)
    print(f"Found {nr_of_words} total words")
    for el in char_counts:
        if el["char"].isalpha():
            print(f"{el['char']}: {el['num']}")
main()
    
    