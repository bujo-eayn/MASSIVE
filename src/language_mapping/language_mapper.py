import os
import json

class LanguageMapper:
    def __init__(self, dataset_folder, output_folder):
        self.dataset_folder = dataset_folder
        self.output_folder = output_folder

    def map_translations(self):
        try:
            # Create output folder if it doesn't exist
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)

            # Define the source (en) language
            source_lang = "en"

            # Initialize a dictionary to store translations
            translations = {}

            # Process all JSONL files in the dataset folder
            for filename in os.listdir(self.dataset_folder):
                if filename.endswith(".jsonl"):
                    with open(os.path.join(self.dataset_folder, filename), "r", encoding="utf-8") as file:
                        for line in file:
                            item = json.loads(line)

                            # Check if the data is for training
                            if item.get("partition") == "train":
                                target_lang = item.get("locale", "xx")  # Default to "xx" if locale is not available
                                if target_lang not in translations:
                                    translations[target_lang] = []
                                translations[target_lang].append({"id": item["id"], "utt": item["utt"]})

            # Write all translation data to a single JSONL file
            output_filename = os.path.join(self.output_folder, f"{source_lang}_to_all_translations.jsonl")
            with open(output_filename, "w", encoding="utf-8") as output_file:
                for target_lang, target_data in translations.items():
                    for translation in target_data:
                        output_file.write(json.dumps(translation, ensure_ascii=False) + "\n")

            print(f"Generated {output_filename}")
            print("Translation mapping completed.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    language_mapper = LanguageMapper("data/", "output")
    language_mapper.map_translations()
