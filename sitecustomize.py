import sys
import os

# Ensure src directory is on sys.path for imports
root = os.path.dirname(__file__)
src_path = os.path.join(root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)
