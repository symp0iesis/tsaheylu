import pandas as pd

# Define chunk size and file paths
chunk_size = 10 ** 6  # Adjust this depending on your machine's memory
input_csv_path = '/home/administrador/Área de Trabalho/tsaheylu/dataset/vxhx934tbn-1/DogMoveData.csv'  # Replace with your CSV file path
output_csv_path = 'reduced_DogMoveData.csv'

# Define the columns to drop
columns_to_drop = ['Task', 'Behavior_2', 'Behavior_3', 'PointEvent']

# Process the CSV in chunks
reader = pd.read_csv(input_csv_path, chunksize=chunk_size)
for i, chunk in enumerate(reader):
    # Filter out rows with "<undefined>" in "Behavior_1"
    chunk_filtered = chunk[chunk['Behavior_1'] != '<undefined>']
    
    # Drop specified columns
    chunk_filtered.drop(columns=columns_to_drop, inplace=True)
    
    # Write the processed chunk to file
    if i == 0:
        # Write headers only on the first chunk
        chunk_filtered.to_csv(output_csv_path, mode='w', index=False)
    else:
        # Append without headers for subsequent chunks
        chunk_filtered.to_csv(output_csv_path, mode='a', index=False, header=False)

    print(f'Processed chunk {i+1}')

print("Dataset reduction complete. Saved as 'reduced_dataset.csv'")

