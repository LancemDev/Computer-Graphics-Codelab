"""
 * This file generates separate lists based on gender
"""
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='./logs/process.log', level=logging.INFO)

# Log start of the process
logging.info('Starting the process.')

# Function to read Excel and combine files
def read_and_combine(files):
    try:
        dfs = [pd.read_excel(f) for f in files]
        combined_df = pd.concat(dfs, ignore_index=True)
        logging.info(f'Files {files} combined successfully.')
        return combined_df
    except Exception as e:
        logging.error(f'Error reading or combining files: {e}')
        raise

# Function to save CSV and TSV files
def save_to_csv_tsv(df, csv_path, tsv_path):
    try:
        df.to_csv(csv_path, index=False)
        df.to_csv(tsv_path, sep='\t', index=False)
        logging.info(f'Saved {csv_path} and {tsv_path} successfully.')
    except Exception as e:
        logging.error(f'Error saving {csv_path} or {tsv_path}: {e}')
        raise

# Read and combine Excel files
df = read_and_combine(['./excel_files/test_file_1.xlsx', './excel_files/test_file_2.xlsx'])

# Separate by gender and save lists
male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']

logging.info(f'Number of male students: {len(male_students)}')
logging.info(f'Number of female students: {len(female_students)}')

save_to_csv_tsv(male_students, './csv_files/male_students_list.csv', './tsv_files/male_students_list.tsv')
save_to_csv_tsv(female_students, './csv_files/female_students_list.csv', './tsv_files/female_students_list.tsv')

# Detect and save names with special characters
special_char_names = df[df['Student Name'].str.contains(r"[^a-zA-Z,\s]", regex=True)]

logging.info(f'Students with special characters: {special_char_names["Student Name"].tolist()}')

save_to_csv_tsv(special_char_names, './csv_files/special_character_names.csv', './tsv_files/special_character_names.tsv')

logging.info('Process completed successfully.')
