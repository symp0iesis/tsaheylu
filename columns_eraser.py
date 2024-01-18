import pandas as pd

# Define chunk size and file paths
chunk_size = 10 ** 6  # Adjust this depending on your machine's memory
input_csv_path = '/home/administrador/Área de Trabalho/tsaheylu/dataset/prepared/DogMoveData_dogids.csv'  # Replace with your CSV file path
output_csv_path = '(neck)DogMoveData_dogids.csv'

# Define the columns to be deleted - replace these with the columns you want to remove
columns_to_delete = ['ABack_x', 'ABack_y', 'ABack_z', 'GBack_x', 'GBack_y', 'GBack_z']  # TODO: Replace with actual column names

# Process the CSV in chunks
reader = pd.read_csv(input_csv_path, chunksize=chunk_size)
for i, chunk in enumerate(reader):
    # Drop specified columns
    chunk_reduced = chunk.drop(columns=columns_to_delete, errors='ignore')
    
    # Write the processed chunk to file
    if i == 0:
        # Write headers only on the first chunk
        chunk_reduced.to_csv(output_csv_path, mode='w', index=False)
    else:
        # Append without headers for subsequent chunks
        chunk_reduced.to_csv(output_csv_path, mode='a', index=False, header=False)

    print(f'Processed chunk {i+1}')

print(f"Dataset columns reduction complete. Saved as '{output_csv_path}'")

