text = input().split(" ")
palindrome = input()
count = 0
print([el for el in text if el == el[::-1]])
for elmnt in text:
    if elmnt == palindrome:
        count += 1
print(f"Found palindrome {count} times")