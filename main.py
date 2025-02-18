with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def count_words(text):
    words = text.split()
    return len(words)



if __name__ == '__main__':
    print(file_contents)
    print(count_words(file_contents))