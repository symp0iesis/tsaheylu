import pandas as pd
from sklearn.model_selection import train_test_split

# Load your dataset
df = pd.read_csv('/home/administrador/Área de Trabalho/tsaheylu/dataset/prepared/(neck)DogMoveData_dogids.csv')

# Split the dataset into training and testing sets (80% train, 20% test)
train_df, test_df = train_test_split(df, test_size=0.2, stratify=df['Behavior_1'], random_state=42)  # 42 is the random seed

# Save the split datasets to new CSV files if needed
train_df.to_csv('(neck)train_dataset.csv', index=False)
test_df.to_csv('(neck)test_dataset.csv', index=False)

