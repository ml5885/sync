from flask import Flask, render_template, request
from rescon.rescon.pipeline import customize_resume

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
    resume = request.files["file"].readlines()
    
    customize_resume(job_desc=job_desc, ideo=ideo, )
    return render_template("html/result.html", data=resume)

if __name__ == "__main__":
    app.run(debug=True)