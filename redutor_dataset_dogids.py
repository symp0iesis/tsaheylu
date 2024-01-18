import pandas as pd

# Define chunk size and file paths
chunk_size = 10 ** 6  # Adjust this depending on your machine's memory
input_csv_path = '/home/administrador/Área de Trabalho/tsaheylu/dataset/reduced_DogMoveData.csv'   # Replace with your CSV file path
output_csv_path = 'reduced_dataset_dogids.csv'

# Define the DogIDs to keep
dog_ids_to_keep = [16, 20, 29, 39, 43, 59]

# Process the CSV in chunks
reader = pd.read_csv(input_csv_path, chunksize=chunk_size)
for i, chunk in enumerate(reader):
    # Filter out rows with the specified DogIDs
    chunk_filtered = chunk[chunk['DogID'].isin(dog_ids_to_keep)]
    
    # Write the processed chunk to file
    if i == 0:
        # Write headers only on the first chunk
        chunk_filtered.to_csv(output_csv_path, mode='w', index=False)
    else:
        # Append without headers for subsequent chunks
        chunk_filtered.to_csv(output_csv_path, mode='a', index=False, header=False)

    print(f'Processed chunk {i+1}')

print("Dataset reduction complete. Saved as 'reduced_dataset_dogids.csv'")

