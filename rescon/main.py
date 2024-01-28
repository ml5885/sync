import os
import re
from flask import Flask, render_template, request, send_file, jsonify
from rescon.lib.pipeline import customize_resume, answer_questions, create_cover_letter
from rescon.lib.formats import TEX_DIR
from rescon.config import server_config
from rescon.sources import switch_scrape

app = Flask(__name__)
DELIMIT = "&&&"

@app.route("/", methods=["GET"])
def index():
    return render_template("html/index.html")

@app.route("/link", methods=["GET"])
def link():
    return render_template("html/link.html")

@app.route("/form", methods=["POST"])
def form():
    link, call = request.form["link"], switch_scrape(request.form["link"])
    if not call:
        return render_template("html/manual.html", text="Unsupported URL.")
    description = call(link).get_description()
    questions = call(link).get_questions()
    questions = [q[0:-1] for q in questions]
    if not (questions or description):
        return render_template("html/manual.html", text="Questions or Description not found.")
    return render_template("html/select.html", questions=DELIMIT.join(questions), description=description, _delimit=DELIMIT)

@app.route("/submit", methods=["POST"])
def submit():
    server_config.openai_api_key = request.form["apiKey"]
    description = request.form["description"]
    keys = request.form.keys()
    keys = [k for k in keys if re.search("question*", k)]
    questions = [request.form[k] for k in keys]
    resume = request.files["file"].readlines()
    resume = [l.decode("utf-8") for l in resume]
    dtf, resume = customize_resume(description, resume)
    qas = answer_questions(questions, resume)
    cl = create_cover_letter(description, resume)
    return render_template("html/result.html", data=dtf, qa=qas, cl=cl)

@app.route("/send/<dtf>", methods=["GET"])
def send(dtf):
    # if not os.path.isfile(f"{TEX_DIR}/{dtf}.tex"):
    #     return "File not found."
    ft = request.args.get("file", None, type=str)
    # if ft == "pdf":
    #     return send_file(f"{TEX_DIR}/{dtf}.pdf", as_attachment=False, mimetype='application/pdf', download_name=f"{dtf}.pdf")
    # elif ft == "tex":
    #     return send_file(f"{TEX_DIR}/{dtf}.tex", as_attachment=False, mimetype='application/x-latex', download_name=f"{dtf}.tex")
    # return "Invalid file type."
    if ft == "pdf":
        return send_file(f"{TEX_DIR}/Tanush_Chopra_resume.pdf", as_attachment=False, mimetype='application/pdf', download_name=f"{dtf}.pdf")
    elif ft == "tex":
        return send_file(f"{TEX_DIR}/Tanush_Chopra_resume.tex", as_attachment=False, mimetype='application/x-latex', download_name=f"{dtf}.tex")
    return "Invalid file type."

if __name__ == "__main__":
    app.run(debug=True)