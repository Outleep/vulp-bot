"""
Jobs handler
"""


import sys
from pathlib import Path

root_path = Path(__file__).parents[2]
sys.path.append(str(root_path))

from ClockParts import Shaft


shaft = Shaft()
shaft.add_cogs("src/jobs/cogs")
