import pandas as pd
#Importing regular expressions(regex)
import re

# Read the Excel data
file_1 = pd.read_excel(r'./excel_files/test_file_1.xlsx')
file_2 = pd.read_excel(r'./excel_files/test_file_2.xlsx')

# Convert to CSV files for easier manipulation
file_1.to_csv('./csv_files/test_csv_file_1.csv', index=False, header=True)
file_2.to_csv('./csv_files/test_csv_file_2.csv', index=False, header=True)

# Load the CSV files again
df_1 = pd.read_csv('./csv_files/test_csv_file_1.csv')
df_2 = pd.read_csv('./csv_files/test_csv_file_2.csv')

# Confirm successful conversion
print('The Excel files have been converted to CSV files.')

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
df_1['Email Address'] = df_1['Student Name'].apply(lambda x: generate_email(x, domain))
df_2['Email Address'] = df_2['Student Name'].apply(lambda x: generate_email(x, domain))

# Save the updated DataFrames with emails to CSV files
df_1.to_csv('./csv_files/test_csv_file_1_with_emails.csv', index=False)
df_2.to_csv('./csv_files/test_csv_file_2_with_emails.csv', index=False)

# Convert CSV files to TSV files
df_1.to_csv('./tsv_files/test_csv_file_1_with_emails.tsv', sep='\t', index=False)
df_2.to_csv('./tsv_files/test_csv_file_2_with_emails.tsv', sep='\t', index=False)

# Confirm successful generation of email addresses and TSV conversion
print('Email addresses have been generated, and CSV files have been converted to TSV format successfully.')
