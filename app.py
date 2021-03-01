from flask import Flask, flash, redirect, render_template, request, session, url_for
from template_generator import Template

app = Flask(__name__)
app.secret_key = "b'\x0cZf\xcdg\xae\x884\xe5F\x08\xb62\x8b\n\xf4'"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fill_in_template")
def fill_in_template():
    session["template"] = request.args.get("template")    
    test = Template(f"static/{session['template']}.txt")
    text = test.get_text()
    items = test.get_items()
    return render_template("fill_in_template.html", text=text, items=items)
        
@app.route("/result", methods = ["POST", "GET"])        
def result():
    test = Template(f"static/{session['template']}.txt")
    filled_text = test.get_text()
    if request.method == "POST":       
        # replace <%%item_name%%> with user input
        for item in test.get_items():
            filled_text = filled_text.replace(f"<%%{item}%%>", request.form[item])
        return render_template("result.html", text=filled_text)
    else:    
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)