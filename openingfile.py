file="test.txt"
with open(file,"w")as file:
    file.write("Testing the write function.\n")
    file.write("Just a test.\n")
    print(f"File sucessfully created and wrote to'{file}'")
    
