file_name = "x-file.txt"
fd = open(file_name)
print("here are the contents of the file:")

for line in fd:
    print(line.replace("\n"", """))
fd.close()
fd = open(file_name)
print("Here are the 3 letter words!")
for line in fd:
    words = line.split()
    for word in words:
        if len(word) == 3:
            print(word)

fd.close()

file_name = "x-file.txt"
fd = open(file_name)  # r is inplicit
print("here are the contents of the file:")


for line in fd:
    #  print(line, end="")
    #  print(line.strip())
    print(line.replace("\n", ""))
fd.close()


#  fd = open(file_name)
with open(file_name) as fd:
    print("Here are the 3 letter words!")
    for line in fd:
        words = line.split()
        for word in words:
            if len(word) == 3:
                print(word)
#  fd.close()