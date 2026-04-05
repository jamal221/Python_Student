import requests
import os

def download_mp3():
    url=input('Web site address:  ')
    save_folder=input('Save folder path:   ')
    filename=input(' The mp3 file name:  ')
    # Create folder if it does not exist
    os.makedirs(save_folder, exist_ok=True)

    # Full path to save the file
    file_path = os.path.join(save_folder, filename)

    # Send request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Write binary content to file
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("Download completed:", file_path)
    else:
        print("Failed to download file")

# Example usage
# mp3_url = "https://www.example.com/sample.mp3"
# save_path = "downloads"
# file_name = "audio.mp3"

download_mp3()
