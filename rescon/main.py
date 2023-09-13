from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    job_desc = request.form["jobDescription"]
    xml_res = request.form["xmlResume"]
    ideo = request.form["ideology"]
    resume = request.files["file"].read()
    print(resume)
    print(job_desc)
    print(xml_res)
    print(ideo)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)