from flask import Flask, render_template, request
from rescon.lib.pipeline import customize_resume

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
    print(job_desc)
    ideo = request.form["ideology"]
    resume = request.files["file"].readlines()
    resume = [l.decode("utf-8") for l in resume]
    customize_resume(job_desc, ideo, resume)
    return render_template("html/result.html", data=resume)

if __name__ == "__main__":
    app.run(debug=True)