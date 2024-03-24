from flask import Flask, render_template, request, jsonify
import json
from transformers import BertForSequenceClassification, BertTokenizerFast, pipeline
import random

app = Flask(__name__)

model_path = "model_arabert"
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizerFast.from_pretrained(model_path)
chatbot = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file = json.load(f)
    return file




intents = load_json_file('intents_arabic.json')

config=load_json_file("model_arabert/config.json")

label2id = config["label2id"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['userInput'].strip().lower()

    # Use the chat function here
    response = chat(chatbot, user_input)

    return jsonify({'response': response})

def chat(chatbot, text):
    print("Chatbot: Hi! I am your virtual assistant. Feel free to ask, and I'll do my best to provide you with answers and assistance.")
    print("Type 'quit' to exit the chat\n\n")

    while text != 'quit':
        score = chatbot(text)[0]['score']

        if score < 0.8:
            print("Chatbot: Sorry I can't answer that\n\n")
            text = input("User: ").strip().lower()
            continue

        label = label2id[chatbot(text)[0]['label']]
        response = random.choice(intents['intents'][label]['responses'])
        return response
        
        #print(f"Chatbot: {response}\n\n")

       # text = input("User: ").strip().lower()


if __name__ == '__main__':
    app.run(debug=True)





















def chat(chatbot, text):
    print("Chatbot: Hi! I am your virtual assistant. Feel free to ask, and I'll do my best to provide you with answers and assistance.")
    print("Type 'quit' to exit the chat\n\n")

    while text != 'quit':
        score = chatbot(text)[0]['score']

        if score < 0.8:
            print("Chatbot: Sorry I can't answer that\n\n")
            text = input("User: ").strip().lower()
            continue

        label = label2id[chatbot(text)[0]['label']]
        response = random.choice(["response1", "response2"])  # Replace with your actual responses
        print(f"Chatbot: {response}\n\n")

        text = input("User: ").strip().lower()

if __name__ == '__main__':
    app.run(debug=True)
