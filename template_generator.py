import sys
class Template(object):   
    def __init__(self, filename):
        self.filename = filename
        self.text, self.items = self.read_file()
    
    @staticmethod
    def to_HTML(text):
        return text.replace("\n", "<br>")
    
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
        text = ""
        with open(self.filename, 'r') as f:
            items = f.readline().split(",")
            # get rid of "\n" for the last item
            items[-1] = items[-1][:-1]
            for line in f:
                text += line
        return text, items
            
    def fill_in_template(self):
        filled_text = self.text
        for item in self.items:
            user_input = input(f"{item}: ")
            filled_text = filled_text.replace(f"<%%{item}%%>", user_input)
        return filled_text
        
    @staticmethod
    def to_HTML(text):
        return text.replace("\n", "<br>")