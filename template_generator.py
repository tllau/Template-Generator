class Template(object):
    def __init__(self, filename):
        self.filename = filename
        self.text, self.items = self.read_file()
    
    def get_text(self):
        return self.text
        
    def get_items(self):
        return self.items

    def read_file(self):
        """ 
        Read a template from a txt file.
        The first line of the file must be a list of items intend for emd-users to be filled in. The rest of the text is the template.
        return: text(str), items(list)
        """
        with open(self.filename, 'r') as f:
            items = f.readline().split(",")
            # get rid of "\n" for the last item
            items[-1] = items[-1][:-1]
            text = f.read()
        return text, items
            
    def fill_in_template(self):
        filled_text = self.text
        for item in self.items:
            user_input = input(f"{item}: ")
            filled_text = filled_text.replace(f"<%%{item}%%>", user_input)
        return filled_text

    
if __name__ == "__main__":
    filename = "templates/reporting_test.txt"
    self_intro = Template(filename)
    print(self_intro.fill_in_template())
    