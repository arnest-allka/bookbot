def countWords(file_contents):
    words = file_contents.split()
    print(len(words))

def countChars(file_contents):
    lowered_char = file_contents.lower()
    char_count = {}

    for char in lowered_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)
    
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    countWords(file_contents)

    countChars(file_contents)

main()