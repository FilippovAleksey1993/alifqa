word = input("word ")
for i in range(1):
    line = input("string ")
    line = line.split(" ")
    for el in line:
        if word in el:
            print(line)
            print(" ".join(line))
            break

# landed on the slopping smuddy shore
