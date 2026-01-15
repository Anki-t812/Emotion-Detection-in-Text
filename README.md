# Emotion Detection in Text

## Overview
This project detects the **emotion expressed in a piece of text**.  
It can classify text into emotions such as *happy, sad, angry, surprise,* etc., helping in sentiment analysis, chatbots, or social media monitoring.

## Approach
The model uses a **TF-IDF vectorizer** to convert text into numerical features and a **Logistic Regression classifier** for prediction.  
Steps:
1. Preprocess text (lowercase, remove punctuation, stopwords)
2. Convert text to TF-IDF vectors
3. Train Logistic Regression on labeled emotion data
4. Predict emotions for new text

## Handling Ambiguity
To handle uncertain predictions, a **confidence threshold** is used:
- If the model’s predicted probability is below the threshold, the emotion is marked as **Neutral**.
## How to Run
Step-by-step

## Future Improvements

