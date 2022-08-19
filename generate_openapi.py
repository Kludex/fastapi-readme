import json
from pathlib import Path

from app.main import app

if __name__ == "__main__":
    with Path("openapi.json").open("w") as f:
        f.write(json.dumps(app.openapi(), indent=2))
