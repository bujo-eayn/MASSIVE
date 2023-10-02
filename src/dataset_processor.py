import os
import json
import threading
from openpyxl import Workbook

class DatasetProcessor:
    def __init__(self, dataset_folder, output_folder):
        self.dataset_folder = dataset_folder
        self.output_folder = output_folder

    def process_dataset(self):
        try:
            # Create output folder if it doesn't exist
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)

            # Read JSONL files and process data
            data = []
            for filename in os.listdir(self.dataset_folder):
                if filename.endswith(".jsonl"):
                    with open(os.path.join(self.dataset_folder, filename), "r", encoding="utf-8") as file:
                        for line in file:
                            data.append(json.loads(line))

            # Group data by locale (language)
            grouped_data = {}
            for item in data:
                lang = item['locale']
                if lang not in grouped_data:
                    grouped_data[lang] = []
                grouped_data[lang].append(item)

            # Function to generate language-specific XLSX file
            def generate_language_xlsx(lang, lang_data):
                output_filename = os.path.join(self.output_folder, f"en-{lang}.xlsx")
                if os.path.exists(output_filename):
                    print(f"Skipping {output_filename} (Already exists)")
                    return

                workbook = Workbook()
                sheet = workbook.active
                sheet.append(["id", "utt", "annot_utt"])
                
                for item in lang_data:
                    sheet.append([item["id"], item["utt"], item["annot_utt"]])

                workbook.save(output_filename)
                print(f"Generated {output_filename}")

            # Generate en-xx.xlsx files in the background
            threads = []
            for lang, lang_data in grouped_data.items():
                thread = threading.Thread(target=generate_language_xlsx, args=(lang, lang_data))
                threads.append(thread)
                thread.start()

            # Wait for all threads to complete
            for thread in threads:
                thread.join()

            print("Language-specific XLSX file generation completed.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    dataset_processor = DatasetProcessor("data/", "output")
    dataset_processor.process_dataset()
