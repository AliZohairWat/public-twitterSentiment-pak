from pathlib import Path
import json

root_path = "C:/Users/User/Documents/Ali/Projects/public-twitterSentiment-pak"

def load_config():
    project_root = Path(root_path)

    config_path = project_root / "config" / "config.json"

    # Load config.json

    with config_path.open() as cf:
        config = json.load(cf)
        new_config = {}
        for path in config:
            new_config[path] = Path(root_path + config[path])
    
    return new_config
