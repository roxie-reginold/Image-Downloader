import os
import requests



def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', ',gif', 'svg']
    for extension in extensions:
        if extension in image_url:
            return extension
        

def download_image(image_url: str, name: str, folder: str = None):
    if extension := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{extension}'
        else:
            image_name: str = f'{name}{extension}'
    else:
        raise Exception('Image extension could not be located!')
    
    #check if file name exists
    if os.path.isfile(image_name): 
        raise Exception('File name already exists!')
    

    #download iamge

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" completed!')
    except Exception as exception:
        print(f'Error: {exception}')    


if __name__ == '__main__':
    input_url: str = input('Enter a url: ')
    input_name: str = input('What would you like to name it?: ')

    print('Dowloading in progress...')
    download_image(input_url, name = input_name, folder='images')