# main.py

from dataset_processor import DatasetProcessor
from file_generator import FileGenerator
from google_drive_integration import GoogleDriveUploader
from language_mapping.language_mapper import map_language_code_to_name, extract_language_code

def main():
    # Initialize dataset processor
    dataset_processor = DatasetProcessor()
    
    # Load and process the dataset
    dataset = dataset_processor.load_dataset()

    # Initialize file generator
    file_generator = FileGenerator()

    # Generate JSONL files
    file_generator.generate_jsonl_files(dataset)

    # Initialize Google Drive uploader
    drive_uploader = GoogleDriveUploader()

    # Upload files to Google Drive if needed
    drive_uploader.upload_file('output/example.json', 'your_drive_folder_id', 'example.json')

if __name__ == "__main__":
    main()
