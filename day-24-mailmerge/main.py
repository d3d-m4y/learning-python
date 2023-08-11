names = None
letter = None
output = None

with open("letter\\letter.txt") as file:
    letter = file.read().splitlines()

with open("names\\names.txt") as file:
    names = file.read().splitlines()

for line in letter:
    for name in names:
        with open(f"output\\letter_for_{name.rstrip()}", "a") as file:
            if "[name]" in line:
                file.write(line.replace("[name],", name + ",\n"))
            else:
                file.write(line + "\n")