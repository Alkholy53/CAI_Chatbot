// bert-model.js

const model_path = "model"; // Adjust the path to your BERT model
const label2id = { 'greeting': 0 }; // Add more labels if needed

const model = transformers.BertForSequenceClassification.from_pretrained(model_path);
const tokenizer = transformers.BertTokenizerFast.from_pretrained(model_path);
const chatbot = transformers.Pipeline("sentiment-analysis", { model: model, tokenizer: tokenizer });

function chat(inputText) {
    return chatbot(inputText);
}
