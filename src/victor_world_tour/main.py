import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))
sys.path.append(str(current_dir.parent))

from generate_final_html import generate_map_html


def main(update_all_locations=False):
    if update_all_locations:
        from get_place_location import get_all_locations
        get_all_locations()

    generate_map_html()
