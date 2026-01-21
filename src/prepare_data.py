from pathlib import Path
import pandas as pd
import emoji
import re 

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "tweet_emotions.csv"

df = pd.read_csv(DATA_PATH)

df=df.drop_duplicates()

def clean_data(text):
  text=text.lower()
  text=re.sub(r'http\S+|www\S+','',text)#url remove no emotion
  text=re.sub(r'@\w+','',text)#mentions remove no emotion
  text=re.sub(r'\d+','',text) #remove integer no emotion in it
  text = emoji.replace_emoji(text, replace='')
  re.sub(r'#(\w+)', r'\1', text)#only # remove
  text = re.sub(r'\s+', ' ', text).strip()#extra spaces
  return text

df['content']=df['content'].astype(str).apply(clean_data)
df.to_csv("data/clean_emotions.csv", index=False)