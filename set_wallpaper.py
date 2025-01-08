import ctypes
import os

def set_wallpaper(image_path):
    # Convert the image path to an absolute path
    abs_image_path = os.path.abspath(image_path)

    # Set the wallpaper using the Windows API
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_image_path, 3)