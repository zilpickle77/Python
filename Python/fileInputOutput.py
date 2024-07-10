filePath='beemovie.txt'
with open(filePath,"r") as filereader:
    content=filereader.readlines()
    print(content, end='')
print(filePath.count("wings"))
# r - Read
# a - Append, adds to end of file
# w - OVERWRITE a file