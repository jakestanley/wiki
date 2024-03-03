import os

from pathlib import Path

class Config:

    _instance = None

    _PAGES_DIR = "pages"
    _HTML_DIR = "public"

    def _create_dirs(self, path: Path):
        self.pages_dir = path.joinpath(self._PAGES_DIR)
        if not os.path.exists(self.pages_dir):
            os.makedirs(self.pages_dir)

        self.html_dir = path.joinpath(self._HTML_DIR)
        if not os.path.exists(self.html_dir):
            os.makedirs(self.html_dir)

    def __init__(self, path: Path = None) -> None:
        if not hasattr(self, 'initialized'):
            if not path:
                raise ValueError("Path not provided to Config constructor")
            self._create_dirs(path)
            self.initialized = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
