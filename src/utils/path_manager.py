import sys
from pathlib import Path
import os

class PathManager:
    def __init__(self):
        self.is_frozen = getattr(sys, 'frozen', False)
        self.BASE_DIR = self.get_base_dir()
        self.DATA_DIR = self.BASE_DIR / "data"
        self.IMAGE_DIR = self.DATA_DIR

    def get_base_dir(self):
        """Obtiene el directorio base del proyecto, dependiendo si está empaquetado o en desarrollo."""
        if self.is_frozen:
            # Si se ejecuta como .exe (empaquetado con PyInstaller)
            return Path(sys._MEIPASS).resolve()
        else:
            # Si se ejecuta como un script en desarrollo
            return Path(__file__).resolve().parent.parent

    def get_image_path(self, image_name):
        """Obtiene la ruta a la imagen."""
        image_path = self.IMAGE_DIR / image_name
        if self.is_frozen:
            # Si está empaquetado, busca la imagen en el directorio temporal
            image_path = Path(sys._MEIPASS) / "data" / image_name
        return str(image_path)
