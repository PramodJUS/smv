import json
import re

# Read the English translation file
with open('Grantha/eng_translation.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Load grantha details to get Sanskrit text
with open('Grantha/grantha-details.json', 'r', encoding='utf-8') as f:
    grantha_details = json.load(f)

# Extract sloka ID and English translation using regex
# Pattern: sloka number followed by text until next sloka number
pattern = r'(\d+-\d+)\.\s+(.*?)(?=\n\d+-\d+\.|$)'
matches = re.findall(pattern, content, re.DOTALL)

print(f"Found {len(matches)} English translations")

# Create dictionary with sloka ID as key
entries_to_rephrase = {}
for sloka_id, translation in matches:
    json_key = sloka_id.replace('-', '.')

    # Only include if exists in grantha-details and has Sanskrit text
    if json_key in grantha_details and 'सुमध्वविजयः' in grantha_details[json_key]:
        sanskrit_text = grantha_details[json_key]['सुमध्वविजयः']
        english_meaning = translation.strip()

        entries_to_rephrase[json_key] = {
            'sanskrit': sanskrit_text,
            'english': english_meaning
        }

print(f"Total entries ready for rephrasing: {len(entries_to_rephrase)}")

# Save in batches of 50
batch_size = 50
batch_num = 1

items = list(entries_to_rephrase.items())
for i in range(0, len(items), batch_size):
    batch = dict(items[i:i+batch_size])

    filename = f'Grantha/rephrase_eng_batch_{batch_num}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

    print(f"Created {filename} with {len(batch)} entries")
    batch_num += 1

print(f"\nCreated {batch_num-1} batch files")
print("Ready to start rephrasing!")
