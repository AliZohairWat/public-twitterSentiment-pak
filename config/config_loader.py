from pathlib import Path
import json

def load_config():
    project_root = Path.cwd()

    config_path = project_root / "config" / "config.json"

    # Load config.json

    with config_path.open() as cf:
        config = json.load(cf)
    
    return config
