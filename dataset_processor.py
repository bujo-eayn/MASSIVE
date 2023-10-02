import pandas as pd  # Importing Pandas for dataset manipulation
import os  # Importing os module to work with file paths

# Load the massive dataset

# List of language codes
languages = ['af-ZA', 'am-ET', 'ar-SA', 'az-AZ', 'bn-BD', 'ca-ES', 'cy-GB', 'da-DK', 'de-DE', 'el-GR', 'en-US', 'es-ES',
             'fa-IR', 'fi-FI', 'fr-FR', 'he-IL', 'hi-IN', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'it-IT', 'ja-JP', 'jv-ID',
             'ka-GE', 'km-KH', 'kn-IN', 'ko-KR', 'lv-LV', 'ml-IN', 'mn-MN', 'ms-MY', 'my-MM', 'nb-NO', 'nl-NL', 'pl-PL',
             'pt-PT', 'ro-RO', 'ru-RU', 'sl-SL', 'sq-AL', 'sv-SE', 'sw-KE', 'ta-IN', 'te-IN', 'th-TH', 'tl-PH', 'tr-TR',
             'ur-PK', 'vi-VN', 'zh-CN', 'zh-TW']  # Add more languages as needed

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Directory containing the JSON files
data_directory = 'data'

# Iterate through each language
for language in languages:
    json_file = os.path.join(data_directory, f'{language}.jsonl')

    # Read and load the JSON file into a DataFrame
    df_language = pd.read_json(json_file, lines=True)

    # Append the language identifier to the 'locale' column
    df_language['locale'] = language

    # Concatenate the data for this language with the combined DataFrame
    combined_df = pd.concat([combined_df, df_language], ignore_index=True)


# Identify Languages with matching IDs

# Assuming you want to identify languages where the IDs match with English (en)
english_id = "0"  # Replace with the English ID you want to match
matching_languages = combined_df[combined_df['id'] == english_id]['locale'].unique()

# Create en-xx.xlxs Files
for language in matching_languages:
    language_df = combined_df[combined_df['locale'] == language]
    output_filename = f'en-{language}.xlxs'
    language_df[['id', 'utt', 'annot_utt']].to_excel(output_filename, index=False)

# Testing and Validation

# Verify the matching languages
print("Matching Languages:")
print(matching_languages)

# Check if the 'en-xx.xlxs' files were created
for language in matching_languages:
    output_filename = f'en-{language}.xlxs'
    if os.path.isfile(output_filename):
        print(f"'{output_filename}' was successfully created.")
    else:
        print(f"'{output_filename}' was not created. Check your code.")

# Verify the contents of the generated 'en-xx.xlxs' files
for language in matching_languages:
    output_filename = f'en-{language}.xlxs'
    language_df = pd.read_excel(output_filename)

    # Display the first few rows of the generated file
    print(f"Contents of '{output_filename}':")
    print(language_df.head())








