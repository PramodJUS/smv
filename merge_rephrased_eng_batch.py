import json
import sys

# Get batch number from command line or default to 1
batch_num = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# Load the rephrased batch
with open(f'Grantha/rephrased_eng_batch_{batch_num}.json', 'r', encoding='utf-8') as f:
    rephrased = json.load(f)

# Load the main grantha details
with open('Grantha/grantha-details.json', 'r', encoding='utf-8') as f:
    grantha_details = json.load(f)

# Merge the rephrased content
for key, content in rephrased.items():
    if key in grantha_details:
        grantha_details[key]["Rephrased English"] = content["rephrased_english"]
        grantha_details[key]["Rephrased Kannada"] = content["rephrased_kannada"]
        print(f"Updated {key}")
    else:
        print(f"Warning: {key} not found in grantha-details.json")

# Save back
with open('Grantha/grantha-details.json', 'w', encoding='utf-8') as f:
    json.dump(grantha_details, f, ensure_ascii=False, indent=2)

print(f"\nBatch {batch_num} merged successfully!")
print(f"Updated {len(rephrased)} entries")
