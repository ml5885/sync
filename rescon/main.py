import os
from flask import Flask, render_template, request, send_file, jsonify
from rescon.lib.pipeline import customize_resume
from rescon.lib.formats import TEX_DIR
from rescon.config import server_config
from rescon.sources import switch_scrape

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("html/index.html")

@app.route("/form", methods=["GET"])
def form():
    return render_template("html/form.html")

@app.route("/submit", methods=["POST"])
def submit():
    server_config.openai_api_key = request.form["openai_api_key"]
    link, call = request.form["link"], switch_scrape(request.form["link"])
    if not call:
        return render_template("html/manual.html")
    resume = request.files["file"].readlines()
    resume = [l.decode("utf-8") for l in resume]
    dtf = customize_resume(job_desc, ideo, resume)
    return render_template("html/result.html", data=dtf)


@app.route("/send/<dtf>", methods=["GET"])
def send(dtf):
    if not os.path.isfile(f"{TEX_DIR}/{dtf}.tex"):
        return "File not found."
    ft = request.args.get("file", None, type=str)
    if ft == "pdf":
        return send_file(f"{TEX_DIR}/{dtf}.pdf", as_attachment=False, mimetype='application/pdf', download_name=f"{dtf}.pdf")
    elif ft == "tex":
        return send_file(f"{TEX_DIR}/{dtf}.tex", as_attachment=False, mimetype='application/x-latex', download_name=f"{dtf}.tex")
    return "Invalid file type."

if __name__ == "__main__":
    app.run(debug=True)