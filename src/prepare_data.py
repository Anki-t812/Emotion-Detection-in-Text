from pathlib import Path
import pandas as pd
import re 

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "tweet_emotions.csv"

df = pd.read_csv(DATA_PATH)

df=df.drop_duplicates()

def remove_mention(text):
  return re.sub(r'@\w+','',text)

df['content']=df['content'].apply(remove_mention)
df.to_csv("data/clean_emotions.csv", index=False)