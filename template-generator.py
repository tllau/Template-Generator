def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text
        
def fill_in_template(filename):
    sample_item = {"date": "26FEB"}
    text = read_file(filename)    
    fill_text = text.replace("{%%date%%}", sample_item["date"])
    return fill_text
    

if __name__ == "__main__":
    filename = "templates/fill_test.txt"
    print(fill_in_template(filename))
    