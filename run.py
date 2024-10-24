"""
Run the main application.

This script serves as the entry point for the victor-world-tour project.
It imports the main function from the src/victor_world_tour/main.py file
and runs it when executed.

Usage:
    python3 run.py

Dependencies:
    - Python 3.9 or higher
    - All dependencies should be installed as specified in the pyproject.toml

Functions:
    - main(): Runs the main logic of the victor_world_tour script.

Note:
    Ensure that the `src` directory is present in the project structure.
"""

from src.victor_world_tour.main import main


if __name__ == '__main__':
    main(update_all_locations=True)
