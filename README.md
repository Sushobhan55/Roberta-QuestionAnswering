# Web Application based on transformer Roberta-Base-Squad2

Grabanswer is a web application that utilizes transformers library from Hugging Face.
Hugging Face's transformers library provides APIs to easily download and train state-of-the-art pretrained models.
You might have heard of GPT-n or BERT that are more popular transformer models. Transformers are good for NLP and image recognition.

Grabanswer utilizes Tinyroberta-Squad2, a distilled version of transformer model Roberta-Base-Squad2. Roberta-Base-Squad2
is a question answering model. The distilled model has a comparable prediction quality and runs at twice the speed of the base model.

You can run it on your local server after installation of all the dependencies in requirements.txt. 

In the web application, you enter a long text and ask a question whose answer is in the text. Then click on the
Grabanswer, it submits your text and question to the model and predicts the answer from the text.

You can use Grabanswer to quickly grab answers from long texts, for example, to get answers to important questions
from a handout or a chapter a night before an exam or to know final exam's date without having to go through entire syllabus; in general,
to answer questions without reading the text. That may save you time. 
