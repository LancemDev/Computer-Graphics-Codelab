# Computer Graphics Codelab

This Codelab processes student data from Excel files, generates email addresses, and creates various output files including CSV, TSV, JSON, and JSONL formats.


## Project Structure
```
project_root/
│
├── excel_files/
│   ├── test_file_1.xlsx
│   └── test_file_2.xlsx
│
├── csv_files/
│   ├── test_csv_file_1.csv
│   ├── test_csv_file_2.csv
│   ├── male_students_list.csv
│   ├── female_students_list.csv
│   └── special_character_names.csv
│
├── tsv_files/
│   ├── test_csv_file_1_with_emails.tsv
│   ├── test_csv_file_2_with_emails.tsv
│   ├── male_students_list.tsv
│   ├── female_students_list.tsv
│   └── special_character_names.tsv
│
├── json_files/
│   ├── shuffled_students.json
│   └── shuffled_students.jsonl
│
├── logs/
│   └── process.log
│
├── main.py
├── functions.py
├── constraints.py
├── generate_emails.py
├── merge_shuffle.py
├── generate_gender_lists.py
├── requirements.txt
└── README.md
```



## Folder Descriptions

- `excel_files/`: Contains the input Excel files with student data.
- `csv_files/`: Stores CSV versions of the Excel files and generated lists.
- `tsv_files/`: Contains TSV versions of the processed data.
- `json_files/`: Stores the final output in JSON and JSONL formats.
- `logs/`: Contains the log file (process.log) with detailed execution information.

## Main Files

- `main.py`: The main script that orchestrates the entire data processing workflow.
- `functions.py`: Contains utility functions used throughout the project.
- `constraints.py`: Defines constants and configuration variables.
- `generate_emails.py`: Handles the generation of email addresses for students.
- `merge_shuffle.py`: Merges and shuffles the processed data.
- `generate_gender_lists.py`: Creates separate lists based on gender and special characters.
- `similarity_check.py`: Checks for similarity between names and emails.

## Functionality

1. Reads student data from Excel files.
2. Converts Excel files to CSV format.
3. Generates email addresses for students.
4. Creates separate lists for male and female students.
5. Identifies and lists students with special characters in their names.
6. Merges and shuffles the processed data.
7. Outputs the final data in JSON and JSONL formats.
8. Logs the entire process for monitoring and debugging.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/LancemDev/Computer-Graphics-Codelab.git
   cd Computer-Graphics-Codelab
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt

## Usage

To run the project, execute the `main.py` script:

```bash 
python main.py
```


This will process the input files and generate all the output files in their respective folders.

## Dependencies

The project dependencies are listed in the `requirements.txt` file. The main dependencies are:

- pandas
- openpyxl (for reading Excel files)

You can install all dependencies using the command provided in the Setup and Installation section.

## Logging

The project logs its progress and any errors in the `logs/process.log` file. Refer to this file for detailed execution information and troubleshooting.

## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

[MIT License](LICENSE)



This will process the input files and generate all the output files in their respective folders.

## Dependencies

- pandas
- openpyxl
- matplotlib
- logging
- json
- transformers
- torch
- sklearn


Install the required dependencies using:

```bash
pip install -r requirements.txt
```


