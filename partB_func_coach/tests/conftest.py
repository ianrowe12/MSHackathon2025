import sys
from pathlib import Path

# Add the project root (one level up from /tests) to sys.path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
