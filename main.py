def countWords(file_contents):
    words = file_contents.split()
    return len(words)

def countChars(file_contents):
    lowered_char = file_contents.lower()
    char_count = {}

    for char in lowered_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
    
def reportBookChars(words,dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    
    keys = list(dict.keys())
    keys.sort()
    sorted_dict = {i: dict[i] for i in keys}
    
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"The {key} character was found {value} times")
            
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(countWords(file_contents))

    # print(countChars(file_contents))
    
    reportBookChars(countWords(file_contents),countChars(file_contents))
    

main()