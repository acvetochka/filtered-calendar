import json

def save_json(data: dict, output_json: str) -> None:
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)