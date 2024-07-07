import genson
import json
import sys

def generate_schema(json_file_path):
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)

    builder = genson.SchemaBuilder()
    builder.add_object(json_data)
    schema = builder.to_schema()

    print(json.dumps(schema, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_schema.py <path_to_json_file>")
        # sys.exit(1)

    json_file_path = sys.argv[1]
    generate_schema(json_file_path)
