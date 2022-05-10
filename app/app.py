from flask import Flask, request, render_template, flash, redirect, url_for

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
		q = request.form['question']
		t = request.form['text']
		return render_template('index.html', answer=grabanswer(q,t))
	else:
		flash('Error Ocuured!')
		return redirect(url_for('/'))

if __name__ == "__main__":
	app.run(debug=True)