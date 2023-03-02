def repeat(word, times):
    for count in range(1, times + 1):
        print(word, end="")


string_word = input()
n = int(input())

repeat(string_word, n)
