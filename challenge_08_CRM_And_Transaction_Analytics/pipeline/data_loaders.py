import json
from typing import Optional

def load_json_file(filepath: str) -> Optional[list[dict]]:
    if not isinstance(filepath, str):
        return None
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return None
