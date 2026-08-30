file="test.txt"
with open(file,"r")as file:
    for line_number,line in enumerate(file,1):
        print(f"Line{line_number}:{line.strip()}")