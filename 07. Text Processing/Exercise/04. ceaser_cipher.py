normal_version = input()
encrypted_version = []

for el in normal_version:
    for parts in el:
        code_of_encrypted_char = ord(parts) + 3
        encrypted_version.append(chr(code_of_encrypted_char))

print("".join(encrypted_version))