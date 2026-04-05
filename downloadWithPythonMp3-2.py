import os
import requests
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint

def download_mp3s():
    page_url = pageEntry.get().strip()
    save_folder = folderEntry.get().strip()

    if not page_url or not save_folder:
        messagebox.showerror("Error", "Please fill all fields")
        return

    os.makedirs(save_folder, exist_ok=True)

    try:
        response = requests.get(page_url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        # pprint(response.raise_for_status())
        # exit()
        

        soup = BeautifulSoup(response.text, "html.parser")
        # pprint(soup)
        # exit()
        mp3_links = set()

        # Find all mp3 links
        for tag in soup.find_all(["a", "audio", "source"]):
            src = tag.get("href") or tag.get("src")
            if src and src.lower().endswith(".mp3"):
                mp3_links.add(urljoin(page_url, src))

        if not mp3_links:
            messagebox.showwarning("No MP3", "No MP3 files found on this page.")
            return

        for mp3_url in mp3_links:
            filename = mp3_url.split("/")[-1]
            file_path = os.path.join(save_folder, filename)

            r = requests.get(mp3_url, stream=True, headers={"User-Agent": "Mozilla/5.0"})
            r.raise_for_status()

            with open(file_path, "wb") as f:
                for chunk in r.iter_content(8192):
                    if chunk:
                        f.write(chunk)

        messagebox.showinfo(
            "Success",
            f"Downloaded {len(mp3_links)} MP3 file(s) successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("MP3 Downloader")
root.geometry("500x200")

tk.Label(root, text="Web Page URL:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
pageEntry = tk.Entry(root, width=50)
pageEntry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Save Folder:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
folderEntry = tk.Entry(root, width=50)
folderEntry.grid(row=1, column=1, padx=5, pady=5)


tk.Button(root, text="Download MP3s", command=download_mp3s, width=20)\
    .grid(row=2, column=1, pady=15)

root.mainloop()
