file="test.txt"
try:
    with open(file,"r")as file:
        content=file.read()
        print("File content\n")
        print(content)
except FileNotFoundError:
    print(f"The file '{file}' was not found.")
except Exception as e:
    print(f"Unknown  error occured {e}")
print()