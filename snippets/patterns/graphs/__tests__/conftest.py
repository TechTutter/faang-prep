# Adds the graphs snippet directory to sys.path so tests can import snippets directly.
# pyproject.toml sets pythonpath = ["patterns/graphs"], which achieves the same effect
# when running via `uv run pytest` from the snippets/ root — this file is a safety net.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
