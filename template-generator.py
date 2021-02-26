def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text
        
def fill_in_template(filename, filled_items):
    text = read_file(filename)
    for item in filled_items:
        text = text.replace(f"<%%{item}%%>", filled_items[item])
    return text
    
def user_form():
    items = ["name", "age", "hobby"]
    filled_items = {}
    for item in items:
        filled_items[item] = input(f"What is your {item}? ")
    return filled_items
    
    
if __name__ == "__main__":
    filename = "templates/user_form_test.txt"
    filled_items = user_form()
    print(fill_in_template(filename, filled_items))
    