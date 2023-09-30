import json
import random

# Define the languages
languages = ['English', 'Swahili', 'German']

# Split the dataset into test, train, and dev data
train_data = []
dev_data = []
test_data = []

for language in languages:
    filtered_dataset = massive_dataset[massive_dataset['target_language'] == language]

    # Split the dataset randomly into train, dev, and test data
    train_data += random.sample(list(filtered_dataset), int(len(filtered_dataset) * 0.8))
    dev_data += random.sample(list(filtered_dataset), int(len(filtered_dataset) * 0.1))
    test_data += random.sample(list(filtered_dataset), int(len(filtered_dataset) * 0.1))

# Generate JSONL files for the train, dev, and test data
for language, data in zip(languages, [train_data, dev_data, test_data]):
    with open(f'{language}.jsonl', 'w') as f:
        for item in data:
            json.dump(item, f)
            f.write('\n')

# Generate a large JSON file showing all the translations from en to xx with id and utt for all the train sets
train_data = pd.concat([train_data, dev_data])

with open('en-xx.jsonl', 'w') as f:
    for item in train_data:
        json.dump({'id': item['id'], 'utt': item['utt'], 'annot_utt': item['annot_utt']}, f)
        f.write('\n')
