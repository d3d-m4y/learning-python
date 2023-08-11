# with open("text") as file:  # with automatically closes the file when done
#     content = file.read()

# print(content)

with open("new_text", mode="w") as file:
    file.write("This is a new file...\n")
    