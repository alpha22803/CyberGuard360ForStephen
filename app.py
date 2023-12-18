from flask import Flask, render_template, Response, request, redirect, url_for

from data.questions import saqa, saqb, saqc, p2pe
from data.elibilityQues import eliA, eliB, eliC, eliP2

app = Flask(__name__, static_url_path='/static')


@app.route('/saqa')
def question():
    return render_template("question.html", saqa=saqa)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/', methods=['POST'])
def handle_button_click():
    global eliQue
    saq_type = request.form.get('saqType')
    if saq_type == 'A':
        eliQue = eliA
    elif saq_type == 'B':
        eliQue = eliB
    elif saq_type == 'C':
        eliQue = eliC
    elif saq_type == 'P2':
        eliQue = eliP2
    print("helo")
    return redirect('/eliQuestions')


@app.route("/eliQuestions")
def eliQuestions():
    return render_template("eliQuestions.html", question=eliQue)


@app.route('/process_answers', methods=['POST'])
def process_answers():
    selected_answers = request.form.getlist('answers[]')
    true_false_values = [answer == "True" for answer in selected_answers]
    print("All are same:", len(eliQue) == len(true_false_values))
    return "Answers received and processed."


@app.errorhandler(404)
def page_not_found(e):
    # snip
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)
