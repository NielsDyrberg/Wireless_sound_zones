from pathlib import Path


def get_project_root() -> Path:
    """
    Used to get project root
    :return: Full path to project
    """
    return Path(__file__).parent.parent

