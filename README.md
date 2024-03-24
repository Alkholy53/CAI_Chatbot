# Demo Chatbot for CAI Website

This repository contains code for building a chatbot for the College of Artificial Intelligence (CAI) website. Two versions of the chatbot are implemented: one in Arabic using the AraBERT model and the other in English using the BERT model.

## Project Overview

The project follows the following steps:

1. Load the data.
2. Exploratory Data Analysis (EDA) and analysis of the data for insights.
3. Split the data into training, testing, and validation datasets.
4. Load the BERT pre-trained model and tokenizer.
5. Transform the data into numerical format.
6. Train the BERT pre-trained model on the custom dataset.
7. Evaluate the model.
8. Save the model.
9. Load the model and start the conversation.

## Installation

To run the code, make sure you have the necessary packages installed:

```bash
pip install -U accelerate transformers xformers
