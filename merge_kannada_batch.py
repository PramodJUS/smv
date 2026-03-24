import csv
import json
import os
import glob

# Find all translated Kannada batch files
batch_pattern = 'Grantha/kannada_translated_batch_*.json'
batch_files = sorted(glob.glob(batch_pattern), key=lambda x: int(x.split('_')[-1].split('.')[0]))

# Load all translated Kannada meanings
kannada_translations = {}
for batch_file in batch_files:
    with open(batch_file, 'r', encoding='utf-8') as f:
        batch_data = json.load(f)
        for item in batch_data:
            key = (item['sarga'], item['sloka_number'])
            kannada_translations[key] = item['kannada']

print(f"Loaded {len(kannada_translations)} Kannada translations from {len(batch_files)} batch files")

# Read current CSV
csv_file = 'Grantha/eng_translations.csv'
rows = []
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    for row in reader:
        key = (row['sarga'], row['sloka_number'])
        if key in kannada_translations:
            row['rephrase_meaningKn'] = kannada_translations[key]
        rows.append(row)

# Write updated CSV
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(rows)

# Calculate progress
total = len(rows)
completed = sum(1 for row in rows if row.get('rephrase_meaningKn', '').strip())
percentage = (completed / total * 100) if total > 0 else 0

print(f"Merged into CSV: {csv_file}")
print(f"Progress: {completed}/{total} ({percentage:.0f}%)")
