from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# akoang list sa mga buhatonon, dri ra ni ma save
# mawala ni sya if i-restart ang app lol, sunod na nako butangan ug database
# format ani kay {"text": "Palit bugas", "done": False}
tasks = [
    {"text": "Practice Python", "done": True},
    {"text": "Tiwas ani nga website", "done": False},
    {"text": "Palit bugas", "done": False},
]

@app.route("/")
def home():
    # para ni sa "2 of 3 tasks done" ba
    done_count = 0
    for t in tasks:
        if t["done"]:
            done_count += 1
    return render_template("index.html", tasks=tasks, done_count=done_count, total=len(tasks))

@app.route("/add", methods=["POST"])
def add():
    # kuhaon ang gi type sa user
    text = request.form.get("task", "").strip()
    if text != "":
        tasks.append({"text": text, "done": False})
    # balik sa home page
    return redirect(url_for("home"))

@app.route("/toggle/<int:index>")
def toggle(index):
    # pindot para ma check / uncheck
    # gi butangan nako ug if para dili mag error if sayop ang index, nag error nako ani sauna haha
    if 0 <= index < len(tasks):
        if tasks[index]["done"]:
            tasks[index]["done"] = False
        else:
            tasks[index]["done"] = True
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    # delete task, sayang wala pay confirm, basin mapislit lol
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("home"))

# pang test lang ni, dagan sa http://127.0.0.1:5000
if __name__ == "__main__":
    app.run(debug=True)
