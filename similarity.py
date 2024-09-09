import pandas as pd
import re
import logging
import json
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

# Set up logging
logging.basicConfig(
    filename='./logs/process.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log start of the process
logging.info('Starting the process.')

try:
    # Read the Excel data
    logging.info('Reading Excel files.')
    file_1 = pd.read_excel(r'./excel_files/test_file_1.xlsx')
    file_2 = pd.read_excel(r'./excel_files/test_file_2.xlsx')
    logging.info('Excel files read successfully.')
except Exception as e:
    logging.error(f'Error reading Excel files: {e}')
    raise

try:
    # Convert to CSV files for easier manipulation
    logging.info('Converting Excel files to CSV.')
    file_1.to_csv('./csv_files/test_csv_file_1.csv', index=False, header=True)
    file_2.to_csv('./csv_files/test_csv_file_2.csv', index=False, header=True)
    logging.info('Excel files converted to CSV successfully.')
except Exception as e:
    logging.error(f'Error converting Excel files to CSV: {e}')
    raise

try:
    # Load the CSV files again
    logging.info('Loading CSV files.')
    df_1 = pd.read_csv('./csv_files/test_csv_file_1.csv')
    df_2 = pd.read_csv('./csv_files/test_csv_file_2.csv')
    logging.info('CSV files loaded successfully.')
except Exception as e:
    logging.error(f'Error loading CSV files: {e}')
    raise

# Merge the DataFrames
merged_df = pd.concat([df_1, df_2], ignore_index=True)

# Extract male and female names
male_names = merged_df[merged_df['Gender'] == 'M']['Student Name'].tolist()
female_names = merged_df[merged_df['Gender'] == 'F']['Student Name'].tolist()

# Load LaBSE model and tokenizer
logging.info('Loading LaBSE model and tokenizer.')
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/LaBSE')
model = AutoModel.from_pretrained('sentence-transformers/LaBSE')

def get_embeddings(names):
    inputs = tokenizer(names, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**inputs).pooler_output
    return embeddings

# Get embeddings for male and female names
logging.info('Generating embeddings for male and female names.')
male_embeddings = get_embeddings(male_names)
female_embeddings = get_embeddings(female_names)

# Compute similarity matrix
logging.info('Computing similarity matrix.')
similarity_matrix = cosine_similarity(male_embeddings, female_embeddings)

# Filter results with at least 50% similarity
threshold = 0.5
similar_pairs = []
for i, male_name in enumerate(male_names):
    for j, female_name in enumerate(female_names):
        similarity_score = similarity_matrix[i, j]
        if similarity_score >= threshold:
            similar_pairs.append({
                'male_name': male_name,
                'female_name': female_name,
                'similarity_score': similarity_score
            })

# Save results to JSON file
logging.info('Saving similarity results to JSON file.')
with open('./json_files/similar_names.json', 'w') as json_file:
    json.dump(similar_pairs, json_file, indent=4)

logging.info('Similarity results saved successfully.')