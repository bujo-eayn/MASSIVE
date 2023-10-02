from dataset_processor import DatasetProcessor
from file_generator import FileGenerator
from google_drive_integration import GoogleDriveUploader
from language_mapping.language_mapper import LanguageMapper

def main():
    # Initialize classes and perform the lab tasks.
    dataset_processor = DatasetProcessor("data/", "output")
    file_generator = FileGenerator("data/", "output")
    google_drive_uploader = GoogleDriveUploader("output")
    language_mapper = LanguageMapper("data/", "output")

    # Task 1: Process MASSIVE dataset and generate en-xx.xlsx files.
    dataset_processor.process_dataset()

    # Task 2: Generate JSONL files for English, Swahili, and German.
    file_generator.generate_language_jsonl_files()

    # Task 3: Map languages if needed.
    language_mapper.map_translations()

    # Task 4: Upload files to Google Drive.
    google_drive_uploader.upload_to_google_drive(["output/en_to_all_translations.jsonl"])
    
if __name__ == "__main__":
    main()
