from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"todo": "Sample Todo", "done": False}]

#Created the routes to render each page of the website
@app.route("/")
def base():
    return render_template("base.html", todos=todos)

@app.route("/index")
def index():
    return render_template("index.html", todos=todos)

@app.route("/contact")
def contact_us():
    return render_template("contact_us.html", todos=todos)

@app.route("/about")
def about_us():
    return render_template("about_us.html", todos=todos)

@app.route("/random")
def random_joke():
    return render_template("random_joke.html", todos=todos)

#Created an 'add' function to add each task to the list, using .requests & .appends 
@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    todos.append({"task" : todo, "done": False})
    return redirect(url_for("index"))
    
@app.route("/check/<int:index>")
def check(index):
    todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
