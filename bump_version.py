import json
from pathlib import Path
from datetime import date

members_file = Path("members.json")

if members_file.exists():
    data = json.loads(members_file.read_text(encoding="utf-8"))
    if isinstance(data, list):
        data = {
            "version": 0,
            "updated_at": "",
            "members": data,
        }
    data["version"] = int(data.get("version", 0)) + 1
else:
    data = {
        "version": 1,
        "updated_at": "",
        "members": [],
    }

data["updated_at"] = str(date.today())

members_file.write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
