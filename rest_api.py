import spacy
import warnings
import en_core_web_sm
from flask import Flask, render_template, request

warnings.filterwarnings("ignore")
nlp = en_core_web_sm.load()

app = Flask(__name__)

def Convert(string):  
	return list(string.split(", "))

def sentence_similarity(input_text):
	print("recived input text:",input_text)
	list_data = []
	my_doc = ""
	for i in range(len(input_text)):
	    max_similarity = 0
	    max_similar_sentence = ""
	    my_doc = nlp(input_text[i])
	    for j in range(len(input_text)):
	        if i!=j:
	            current_similarity = my_doc.similarity(nlp(input_text[j]))
	            if max_similarity < current_similarity:
	                max_similarity = current_similarity
	                max_similar_sentence = input_text[j]
	    temp_data = [f"{input_text[i]}",f"{max_similar_sentence}"]
	    list_data.append(temp_data)
	return list_data

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/input', methods = ['POST'])
def input():
	if request.method == 'POST':
		input_text = request.form.get("input_text_sentences")
		input_text = Convert(input_text.replace("[","").replace("]","").replace('"',''))
		# print(sentence_similarity(input_text))
	return render_template("jinja.htm",data = sentence_similarity(input_text))

if __name__ == "__main__":
	app.run(debug = True)