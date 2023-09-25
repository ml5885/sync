from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("html/index.html")

@app.route("/form", methods=["GET"])
def form():
    return render_template("html/form.html")

@app.route("/submit", methods=["POST"])
def submit():
    job_desc = request.form["jobDescription"]
    ideo = request.form["ideology"]
    resume = request.files["file"]
    print(resume)
    print(job_desc)
    print(ideo)
    return render_template("html/index.html", data=job_desc)

if __name__ == "__main__":
    app.run(debug=True)