def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    count_character(text)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_character(text):
    char_dict = dict()
    for character in text:
        if character.isalpha():
            if character.lower() in char_dict:
                char_dict [character.lower()] += 1
            else:
                char_dict [character.lower()] = 1

    char_list = []
    for e in char_dict:
        char_info = {'char': e, 'num': char_dict[e]}
        char_list.append(char_info)
    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

def sort_on(dict):
    return dict["num"]
main()