"""
This file contains the main function to run the program.
"""

import pandas as pd
import logging

from constraints import *
from functions import *

def main():
    setup_logging()
    
    # Process Excel files
    dataframes = []
    for i, excel_file in enumerate(EXCEL_FILES):
        df = read_excel_file(excel_file)
        
        # Print column names for debugging
        print(f"Columns in DataFrame {i+1}: {df.columns.tolist()}")
        
        # Determine the correct name column
        name_column = 'Student Name' if 'Student Name' in df.columns else 'Name'
        
        df = generate_emails_for_dataframe(df, name_column, EMAIL_DOMAIN)
        save_dataframe_to_csv(df, CSV_FILES_WITH_EMAILS[i])
        convert_csv_to_tsv(df, TSV_FILES[i])
        dataframes.append(df)
    
    # Merge, shuffle, and process final dataframe
    merged_df = merge_and_shuffle_dataframes(dataframes)
    merged_df = add_special_characters_column(merged_df, name_column)
    final_df = create_final_dataframe(merged_df)
    
    # Save as JSON and JSONL
    save_as_json(final_df, JSON_OUTPUT)
    save_as_jsonl(final_df, JSONL_OUTPUT)

    logging.info('Process completed successfully.')

if __name__ == "__main__":
    main()