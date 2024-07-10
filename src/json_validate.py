import json

def validate_jsonl_file(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Error in entry at line {line_number}: Invalid JSON - {e}")

# Call the function with your JSONL file path
validate_jsonl_file("../data/ai_script_writer.jsonl")