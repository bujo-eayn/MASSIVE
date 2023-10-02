import os
import json

class FileGenerator:
    def __init__(self, dataset_folder, output_folder):
        self.dataset_folder = dataset_folder
        self.output_folder = output_folder

    def generate_language_jsonl_files(self):
        try:
            # Create output folder if it doesn't exist
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)

            # Define the languages and partitions to generate
            languages = ["en", "sw", "de"]
            partitions = ["test", "train", "dev"]

            for lang in languages:
                for partition in partitions:
                    output_filename = os.path.join(self.output_folder, f"{lang}-{partition}.jsonl")

                    # Check if the file already exists, if so, skip
                    if os.path.exists(output_filename):
                        print(f"Skipping {output_filename} (Already exists)")
                        continue

                    # Filter and write data for the specific language and partition
                    data = []
                    for filename in os.listdir(self.dataset_folder):
                        if filename.startswith(f"{lang}-") and filename.endswith(".jsonl"):
                            with open(os.path.join(self.dataset_folder, filename), "r", encoding="utf-8") as file:
                                for line in file:
                                    item = json.loads(line)
                                    if item["partition"] == partition:
                                        data.append(item)

                    # Write filtered data to the output JSONL file
                    with open(output_filename, "w", encoding="utf-8") as output_file:
                        for item in data:
                            output_file.write(json.dumps(item) + "\n")

                    print(f"Generated {output_filename}")

            print("Language-specific JSONL file generation completed.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_generator = FileGenerator("data/", "output/json")
    file_generator.generate_language_jsonl_files()
