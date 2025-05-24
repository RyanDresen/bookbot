from stats import get_num_words, get_char_count,sort_list_of_dicts
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        text = get_book_text(sys.argv[1])
    return text

print('''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------''')
get_num_words(main())
print('--------- Character Count -------')
sort_list_of_dicts(get_char_count(main()))
print('============= END ===============')
