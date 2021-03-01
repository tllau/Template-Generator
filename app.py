from flask import Flask, flash, redirect, render_template, request, session, url_for
from template_generator import Template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fill_in_template", methods = ["POST", "GET"])
def fill_in_template():
    if request.method == "POST":
        test = Template("static/user_form_test.txt")
        text = test.get_text()
        items = test.get_items()
        return render_template("fill_in_template.html", text=text, items=items)
    else:    
        return redirect("/")
        
@app.route("/result", methods = ["POST", "GET"])        
def result():
    test = Template("static/user_form_test.txt")
    filled_text = test.get_text()
    if request.method == "POST":
        # replace <%%item_name%%> with user input
        for item in test.get_items():
            filled_text = filled_text.replace(f"<%%{item}%%>", request.form[item])
        return render_template("result.html", text=filled_text)
    else:    
        return redirect("/")

if __name__ == "__main__":
    test = Template("static/user_form_test.txt")
    app.run(debug=True)