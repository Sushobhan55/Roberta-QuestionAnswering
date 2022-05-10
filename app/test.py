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

print(grabanswer("what is economics?","Economics is the social science that studies the production, distribution, and consumption of goods and services. Economics focuses on the behaviour and interactions of economic agents and how economies work. Microeconomics is a field which analyzes what's viewed as basic elements"))