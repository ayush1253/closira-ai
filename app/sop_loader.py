import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOP_PATH = os.path.join(BASE_DIR, "data", "sop.json")


def load_sop():
    with open(SOP_PATH, "r") as f:
        return json.load(f)