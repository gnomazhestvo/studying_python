from pathlib import Path
import json

path = Path('numbers.json')
content = path.read_text()
print(content)
numbers = json.loads(content)
print(content)