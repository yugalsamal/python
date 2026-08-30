file="test.txt"
with open(file,"a")as file:
    file.write("Appending the file that was created previously.")
print(f"Successfully appended the file '{file}")
