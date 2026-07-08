import json
from pathlib import Path
from datetime import date

version_file = Path("version.json")

if version_file.exists():
    data = json.loads(version_file.read_text(encoding="utf-8"))
    version = int(data.get("version", 0)) + 1
else:
    version = 1

data = {
    "version": version,
    "updated_at": str(date.today())
}

version_file.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8"
)