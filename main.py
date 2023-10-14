import os
import requests
from pathlib import Path

def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', ',gif', 'svg']
    for extension in extensions:
        if extension in image_url:
            return extension

def download_image(image_url: str, name: str):
    # Get the path to the "Downloads" folder
    downloads_folder = str(Path.home() / "Downloads")

    # Get the file extension
    extension = get_extension(image_url)
    if not extension:
        raise Exception('Image extension could not be located!')

    # Create the full path for the image file
    image_name = os.path.join(downloads_folder, f'{name}{extension}')

    # Check if the file name exists
    if os.path.isfile(image_name):
        raise Exception('File name already exists!')

    # Download the image
    try:
        image_content = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
        print(f'Downloaded: "{image_name}" completed!')
    except Exception as exception:
        print(f'Error: {exception}')


if __name__ == '__main__':
    input_url = input('Enter a URL: ')
    input_name = input('What would you like to name it?: ')

    print('Downloading in progress...')
    download_image(input_url, name=input_name)