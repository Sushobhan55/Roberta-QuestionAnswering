from flask import Flask, request, render_template

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/tinyroberta-squad2"

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def grabanswer(q,t):
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {'question': q, 'context': t}
    res = nlp(QA_input)
    return res['answer']

app = Flask(__name__)

app.secret_key= 'bananaappleargalisacha'

@app.route('/', methods=["GET","POST"])
def main():
	if request.method == "GET":
		return render_template('index.html')
	if request.method == "POST":
		return render_template('index.html',
							   text=request.form['text'],
							   question=request.form['question'],
							   answer=grabanswer(request.form['question'],request.form['text']))

@app.route("/contact/")
def contact():
	return render_template("contact.html")

@app.route("/about/")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)