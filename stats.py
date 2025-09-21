import string
import sys


    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        path_to_file = f.read()

    return path_to_file


def word_count():
    words_list = get_book_text(sys.argv[1])
    words = words_list.split()

    num_words = len(words)
    
    return num_words


def character_count():
    words_list = get_book_text(sys.argv[1])
    lower_case_words = words_list.lower()
    words = lower_case_words.split()
    
    characters = []
    extras = {'æ', 'â', 'ê', 'ë', 'ô'}
    alphabet = set(string.ascii_lowercase) | extras
    character_dictionary = dict.fromkeys(alphabet, 0)

    for word in words:
        for char in word:
            characters.append(char)

    for character in characters:
        if character in alphabet:
            character_dictionary[character] += 1
        
    
    return character_dictionary

def words_report():
    
    words_list = character_count()
    words_sorted = dict(sorted(words_list.items(), reverse=True, key=lambda kv: kv[1]))

    for key, value in sorted(words_sorted.items(), reverse=True, key=lambda kv: kv[1]):
        print(f"{key}: {value}")

    

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print("Found", word_count(), "total words")
    print("--------- Character Count -------")
    words_report()
    


main()
