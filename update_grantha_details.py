import json
import csv

# Read CSV data
csv_file = 'Grantha/eng_translations.csv'
meanings = {}

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = f"{row['sarga']}.{row['sloka_number']}"
        meanings[key] = {
            'english': row['meaning'],
            'kannada': row['rephrase_meaningKn']
        }

print(f"Loaded {len(meanings)} meanings from CSV")

# Read grantha-details.json
json_file = 'Grantha/grantha-details.json'
with open(json_file, 'r', encoding='utf-8') as f:
    grantha_data = json.load(f)

# Update the JSON data
updated_count = 0
for key in grantha_data:
    if key in meanings:
        # Update Meaning - English and Meaning - Kannada
        grantha_data[key]['Meaning - English'] = meanings[key]['english']
        grantha_data[key]['Meaning - Kannada'] = meanings[key]['kannada']

        # Remove Rephrased fields
        if 'Rephrased English' in grantha_data[key]:
            del grantha_data[key]['Rephrased English']
        if 'Rephrased Kannada' in grantha_data[key]:
            del grantha_data[key]['Rephrased Kannada']

        updated_count += 1

print(f"Updated {updated_count} slokas")

# Write updated JSON back
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(grantha_data, f, ensure_ascii=False, indent=2)

print(f"Updated {json_file}")
print("Removed 'Rephrased English' and 'Rephrased Kannada' fields")
print("Populated 'Meaning - English' and 'Meaning - Kannada' from CSV")
