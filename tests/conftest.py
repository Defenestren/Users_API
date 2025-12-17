import sys
from pathlib import Path

# Añade la raíz del proyecto al PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
