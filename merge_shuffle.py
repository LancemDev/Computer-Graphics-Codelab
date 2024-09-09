"""
 * This file merges, shuffles and saves the names of the students
"""
import pandas as pd
import json
import logging

# Set up logging
logging.basicConfig(
    filename='./logs/process.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def read_and_merge_csv(files):
    """Read and merge CSV files into a single DataFrame."""
    logging.info('Reading and merging CSV files.')
    dfs = [pd.read_csv(file) for file in files]
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df

def shuffle_and_save(df, json_file, jsonl_file):
    """Shuffle DataFrame and save to JSON and JSONL files."""
    logging.info('Shuffling DataFrame.')
    shuffled_df = df.sample(frac=1).reset_index(drop=True)

    # Save as JSON
    logging.info(f'Saving shuffled data to {json_file}.')
    shuffled_df.to_json(json_file, orient='records', indent=4)

    # Prepare and save as JSONL
    logging.info('Preparing data for JSONL format.')
    jsonl_data = []
    for idx, row in shuffled_df.iterrows():
        special_character = 'yes' if any(
            char in row['Student Name'] for char in ['\'', '-', '‘', '’', '“', '”', '(', ')']) else 'no'
        jsonl_data.append({
            "id": str(idx),
            "student_number": row['Student Number'],
            "additional_details": [
                {
                    "dob": row['DoB'],
                    "gender": row['Gender'].lower(),
                    "special_character": special_character,
                    "name_similar": "no"  # Placeholder for name similarity logic
                }
            ]
        })

    logging.info(f'Saving data to {jsonl_file}.')
    with open(jsonl_file, 'w') as f:
        for entry in jsonl_data:
            f.write(json.dumps(entry) + '\n')


def main():
    try:
        files = ['./csv_files/test_csv_file_1_with_emails.csv', './csv_files/test_csv_file_2_with_emails.csv']
        merged_df = read_and_merge_csv(files)
        shuffle_and_save(
            merged_df,
            './json_files/shuffled_students.json',
            './json_files/shuffled_students.jsonl'
        )
        logging.info('Process completed successfully.')
    except Exception as e:
        logging.error(f'Error during the process: {e}')


if __name__ == '__main__':
    main()
