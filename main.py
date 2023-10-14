import os
import requests



def get_extension(image_irl: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', ',gif', 'svg']
    for extension in extensions:
        if extension in image_irl:
            return extension
        

def download_image(image_url: str, name: str, folder: str = None):
    if e