def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_word(file_contents):
    num_word = len(file_contents.split())
    return num_word

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c != " ":
            c_lower = c.lower()
            if c_lower in chars:
                chars[c_lower] += 1
            else:
                chars[c_lower] = 1
    return chars

def sort_on(items):
    return items["num"]

def get_chars_list(dict):
    new_list = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        new_list.append(new_dict)
    return new_list
    
def get_chars_list_sorted(list):
    list.sort(reverse=True, key=sort_on)
    return list