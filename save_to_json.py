import json
from typing import List, Dict, Any

def save_to_json(data: List[Dict[str, Any]], filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False) 