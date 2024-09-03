import pandas as pd
import re
import logging

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

# Domain for email addresses
domain = "gmail.com"

def generate_email(name, domain):
    # Adjusted regex to match "Last, First Middle" format
    match = re.match(r"([\w']+),\s+([\w]+)", name)
    if match:
        last_name = match.group(1).lower()
        first_name_initial = match.group(2)[0].lower()  # Get the first letter of the first name

        # Format the email as "first_initiallastname@gmail.com"
        email = f"{first_name_initial}{last_name}@{domain}"
        return email
    else:
        return 'invalid@example.com'

# Apply the function to generate emails
try:
    logging.info('Generating email addresses.')
    df_1['Email Address'] = df_1['Student Name'].apply(lambda x: generate_email(x, domain))
    df_2['Email Address'] = df_2['Student Name'].apply(lambda x: generate_email(x, domain))
    logging.info('Email addresses generated successfully.')
except Exception as e:
    logging.error(f'Error generating email addresses: {e}')
    raise

try:
    # Save the updated DataFrames with emails to CSV files
    logging.info('Saving updated CSV files with email addresses.')
    df_1.to_csv('./csv_files/test_csv_file_1_with_emails.csv', index=False)
    df_2.to_csv('./csv_files/test_csv_file_2_with_emails.csv', index=False)
    logging.info('Updated CSV files saved successfully.')
except Exception as e:
    logging.error(f'Error saving updated CSV files: {e}')
    raise

try:
    # Convert CSV files to TSV files
    logging.info('Converting CSV files to TSV format.')
    df_1.to_csv('./tsv_files/test_csv_file_1_with_emails.tsv', sep='\t', index=False)
    df_2.to_csv('./tsv_files/test_csv_file_2_with_emails.tsv', sep='\t', index=False)
    logging.info('CSV files converted to TSV format successfully.')
except Exception as e:
    logging.error(f'Error converting CSV files to TSV: {e}')
    raise

# Confirm successful generation of email addresses and TSV conversion
logging.info('Email addresses have been generated, and CSV files have been converted to TSV format successfully.')
