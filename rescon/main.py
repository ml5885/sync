from flask import Flask, render_template, request, send_file
from rescon.lib.pipeline import customize_resume
from rescon.lib.formats import TEX_DIR

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
    resume = [l.decode("utf-8") for l in resume]
    # dtf = customize_resume(job_desc, ideo, resume)
    dtf = 1695863133.296293
    return render_template("html/result.html", data=dtf)


@app.route("/send-file", methods=["GET"])
def sendFile():
    return send_file(f"{TEX_DIR}/{dtf}.pdf", as_attachment=True, mimetype='application/pdf', download_name=f"{dtf}.pdf")

if __name__ == "__main__":
    app.run(debug=True)