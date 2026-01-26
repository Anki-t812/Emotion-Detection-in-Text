from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

BASE_DIR=Path(__file__).resolve().parent.parent
DATA_PATH=BASE_DIR/"data"/"clean_emotions.csv"

df=pd.read_csv(DATA_PATH)

df = df.dropna(subset=['content', 'sentiment'])
##Splitiing of dataset
X=df['content']
y=df['sentiment']

X_train,X_test,y_train,y_test=train_test_split(
  X,                #input data
  y,                # label or output
  test_size=0.2,    # split size
  stratify=y,       #same proportion on both test and train
  random_state=42   #for consistency of train_test
)

vectorizer=TfidfVectorizer(
  max_features=10000,   # max words in the dic of model
  stop_words='english', # removes common words from language
  ngram_range=(1,2)     # that many words will be taken like 'very good'&'not good'
)
X_train_tfidf=vectorizer.fit_transform(X_train)#learns vocab and calc TFIDF

X_test_tfidf=vectorizer.transform(X_test)#use the vocab and ignore new words
print(f"Matrix Shape: {X_train_tfidf.shape}")