file_path = input().split(".")

file_extension = file_path[1]
file_path.remove(file_extension)
print(f"File extension: {file_extension}")

x = "".join(file_path)

slash_split = x.split("\\")
file_name = slash_split[-1]
print(f"File name: {file_name}")
