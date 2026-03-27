from pathlib import Path

BASE_DIR = Path(__file__).parent

def project_path(path: str) -> Path:
    return BASE_DIR / Path(path)