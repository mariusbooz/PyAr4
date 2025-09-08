import os, yaml

def load_config():
    CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                            "config", "settings.yaml")  

    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)
