def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    print(text)
        

if __name__ == "__main__":
    filename = "templates/test.txt"
    read_file(filename)