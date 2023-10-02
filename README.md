# MASSIVE

## Overview
Our Solution demonstrates the use of OOP principles to successfully process the MASSIVE dataset, generated required files, and integrated Google Drive uploading into our workflow.

## Folder Structure

    ```bash
        massive/
        │
        ├── data/
        │   ├── jsonl_data/
        │   │   ├── en-US.jsonl
        │   │   ├── te-IN.jsonl
        │   │   ├── ...
        │   │   └── (other language codes).jsonl
        │
        ├── src/
        │   ├── __init__.py
        │   ├── dataset_processor.py
        │   ├── file_generator.py
        │   ├── google_drive_integration.py
        │   ├── language_mapping/
        │   │   ├── __init__.py
        │   │   ├── language_mapper.py
        │   └── main.py
        │
        ├── output/
        │
        ├── actions_scripts/
        │   ├── contributors.py
        │
        ├── .github/
        │   ├── workflows/
        │   │   ├── update_contributors.yml
        │
        ├── README.md
    ```

## Instructions
Dependencies that need to be installed or set up before proceeding.

- Python 3.x
- Pandas
- pydrive

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/bujo-eayn/massive.git
   ```

2. Navigate to the project directory:

    ```bash
    cd massive
    ```
3. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
4. Run Project
    ```bash
    python /src/main.py
    ```

## Components
The following are the main Modules of our Project.

### 1. Main Processor
We provide logic in the main.py file to initialize all the classes and call there methods. These methods receive the required parameters to execute their individual functions.

### 2. Dataset Processor
We created a class named DatasetProcessor in the dataset_processor.py file. This class handles the generation of language-specific Excel files. It reads JSONL files in the data/ folder, extracts relevant data (id, utt, annot_utt), and groups the data by language. For each language, it generates an Excel file with the language code appended to "en-" (e.g., "en-te-IN.xlsx").
This is a long process that stalls the program execution hence our use of threads to allow for program execution as this process continues.
We also implement logic to ensure files that already exist are not generated again to save on time.

### 3. File Generator
We created the FileGenerator class in file_generator.py to generate separate JSONL files for English (en), Swahili (sw), and German (de) for test, train, and dev data. You used filtering to extract the desired data from the input JSONL files.

### 4. Language Mapper
We created a class named LanguageMapper in language_mapper.py. This class processes the JSONL files in the data/ folder, maps translations from English (en) to all languages (xx), and generates a large JSONL file (en_to_all_translations.jsonl) containing the mapped translations.

### 5. Google Drive Integration
We included code for uploading files to Google Drive using the GoogleDriveUploader class. This class handles Google Drive authentication and file upload.
We utilize the client_secrets.json file for security

## Authors
List the project authors and contributors.
* 125672 - Job Ian
* 146685      Victor Mutunga
* 145184     Johnny Ngare
* 136723      David Kungu
* 135358      Sheldon Ngetich
