"""
 * This file contains the functions necessary for the program to run.
"""
## Generate Email Addresses functions

import pandas as pd
import re
import logging
import json
from constraints import *

# Set up logging
def setup_logging():
    logging.basicConfig(
        filename='./logs/process.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Domain for email addresses
EMAIL_DOMAIN = "gmail.com"

def read_excel_file(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        logging.error(f'Error reading Excel file {file_path}: {e}')
        raise

def convert_excel_to_csv(df, output_path):
    try:
        df.to_csv(output_path, index=False, header=True)
    except Exception as e:
        logging.error(f'Error converting Excel to CSV {output_path}: {e}')
        raise

def read_csv_file(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        logging.error(f'Error reading CSV file {file_path}: {e}')
        raise

def generate_email(name, domain):
    match = re.match(r"([\w']+),\s+([\w]+)", name)
    if match:
        last_name = match.group(1).lower()
        first_name_initial = match.group(2)[0].lower()
        return f"{first_name_initial}{last_name}@{domain}"
    else:
        return 'invalid@example.com'


def generate_emails_for_dataframe(df, name_column, domain):
    try:
        # Print column names for debugging
        print(f"Columns in the DataFrame: {df.columns.tolist()}")
        
        # Check if the name_column exists
        if name_column not in df.columns:
            raise KeyError(f"Column '{name_column}' not found in the DataFrame")
        
        # Generate email addresses
        df['Email Address'] = df[name_column].apply(lambda x: generate_email(x, domain))
        
        # Generate gender lists
        male_students = df[df['Gender'] == 'M']
        female_students = df[df['Gender'] == 'F']

        logging.info(f'Number of male students: {len(male_students)}')
        logging.info(f'Number of female students: {len(female_students)}')

        # Save gender lists to CSV and TSV
        male_students.to_csv(MALE_STUDENTS_CSV, index=False)
        male_students.to_csv(MALE_STUDENTS_TSV, sep='\t', index=False)
        female_students.to_csv(FEMALE_STUDENTS_CSV, index=False)
        female_students.to_csv(FEMALE_STUDENTS_TSV, sep='\t', index=False)

        logging.info(f'Saved gender lists to CSV and TSV files.')

        # Detect and save names with special characters
        special_char_names = df[df[name_column].str.contains(r"[^a-zA-Z,\s]", regex=True)]
        logging.info(f'Students with special characters: {special_char_names[name_column].tolist()}')

        special_char_names.to_csv(SPECIAL_CHAR_CSV, index=False)
        special_char_names.to_csv(SPECIAL_CHAR_TSV, sep='\t', index=False)

        logging.info(f'Saved special character names to CSV and TSV files.')

        return df
    except Exception as e:
        logging.error(f'Error in generate_emails_for_dataframe: {e}')
        raise

def save_dataframe_to_csv(df, output_path):
    try:
        df.to_csv(output_path, index=False)
    except Exception as e:
        logging.error(f'Error saving CSV file {output_path}: {e}')
        raise

def convert_csv_to_tsv(df, output_path):
    try:
        df.to_csv(output_path, sep='\t', index=False)
    except Exception as e:
        logging.error(f'Error converting CSV to TSV {output_path}: {e}')
        raise

def merge_and_shuffle_dataframes(df_list):
    merged_df = pd.concat(df_list, ignore_index=True)
    return merged_df.sample(frac=1).reset_index(drop=True)

def add_special_characters_column(df, name_column):
    df['special_characters'] = df[name_column].apply(lambda x: bool(re.search(r"[^\w\s,']", x)))
    return df

def create_final_dataframe(df):
    final_df = df.rename(columns={
        'No.': 'id',
        'Student Number': 'student_number',
        'DoB': 'dob',
        'Gender': 'gender'
    })[['id', 'student_number', 'dob', 'gender', 'special_characters']]

    final_df['additional_details'] = final_df.apply(lambda row: [{
        'dob': row['dob'],
        'gender': row['gender'],
        'special_characters': row['special_characters']
    }], axis=1)

    return final_df.drop(columns=['dob', 'gender', 'special_characters'])

def save_as_json(df, output_path):
    def convert_timestamps(obj):
        if isinstance(obj, pd.Timestamp):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, dict):
            return {k: convert_timestamps(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_timestamps(i) for i in obj]
        return obj

    df_copy = df.copy()
    for column in df_copy.columns:
        df_copy[column] = df_copy[column].apply(convert_timestamps)
    
    json_data = json.dumps(df_copy.to_dict(orient='records'), indent=4, default=str)
    with open(output_path, 'w') as json_file:
        json_file.write(json_data)

def save_as_jsonl(df, output_path):
    def convert_timestamps(obj):
        if isinstance(obj, pd.Timestamp):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, dict):
            return {k: convert_timestamps(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_timestamps(i) for i in obj]
        return obj

    with open(output_path, 'w') as jsonl_file:
        for record in df.to_dict(orient='records'):
            converted_record = convert_timestamps(record)
            jsonl_file.write(json.dumps(converted_record) + '\n')


