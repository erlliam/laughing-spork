import sys

word = sys.argv[0]

def reverse_word(word):
    word_list = []
    for character in word:
        word_list.append(character)
    print(word_list)
    print(len(word_list))
    length = len(word_list)
    test = []
    for index, value in enumerate(word):
        print(index)
        test[length - 1] = value
    print(test)
reverse_word(word)
