file=open("This is a file.","w")

file.write("This is the first line of text.\n")
file.write("This is the second line of text.\n")

file.close

with open(file,"r") as file:
    for line in file:
        current_line=line.strip()
        print(current_line)

file=open("existing_file.txt","a")
file.write("This is a text.\n")
file.close()