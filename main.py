from stats import count_word, get_book_text, get_chars_dict, get_chars_list, get_chars_list_sorted
import sys

def main():
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(file_path)
    num_word = count_word(text)
    dict = get_chars_dict(text)
    list = get_chars_list(dict)
    sorted_list = get_chars_list_sorted(list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i['char'].isalpha():
            key = i['char']
            value = i['num']
            print(f"{key}: {value}")
    print("============= END ===============")

main()