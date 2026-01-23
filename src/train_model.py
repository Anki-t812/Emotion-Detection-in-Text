from pathlib import Path
from sklearn.model_selection import train_test_split
import pandas as pd

BASE_DIR=Path(__file__).resolve().parent.parent
DATA_PATH=BASE_DIR/"data"/"clean_emotions.csv"

df=pd.read_csv(DATA_PATH)

X=df['content']
y=df['sentiment']

X_train,X_test,y_train,y_test=train_test_split(
  X,                #input data
  y,                # label or output
  test_size=0.2,    # split size
  stratify=y,       #same proportion on both test and train
  random_state=42   #for consistency of train_test
)
print("Original distribution:")
print(y.value_counts(normalize=True))

print("\nTrain distribution:")
print(y_train.value_counts(normalize=True))

print("\nTest distribution:")
print(y_test.value_counts(normalize=True))
