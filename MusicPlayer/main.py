import os
import random
import tkinter as tk
from tkinter import ttk, messagebox
from pygame import mixer
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC
from datetime import datetime

mixer.init()

MOOD_DIR = "moods"

MOODS = {
    "😊 شاد": "happy",
    "😢 غمگین": "sad",
    "😏 حماسی": "epic",
    "😴 خسته": "tired"
}

def get_metadata(filepath):
    try:
        audio = MP3(filepath, ID3=ID3)
        length = int(audio.info.length)
        minutes = length // 60
        seconds = length % 60
        metadata = {
            "title": audio.get("TIT2", "نام آهنگ: نامشخص"),
            "artist": audio.get("TPE1", "خواننده: نامشخص"),
            "album": audio.get("TALB", "آلبوم: نامشخص"),
            "year": audio.get("TDRC", "سال ساخت: نامشخص"),
            "duration": f"{minutes}:{seconds:02d}"
        }
        return metadata
    except Exception as e:
        return {
            "title": "نام آهنگ: نامشخص",
            "artist": "خواننده: نامشخص",
            "album": "آلبوم: نامشخص",
            "year": "سال ساخت: نامشخص",
            "duration": "نامشخص"
        }

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("موزیک پلیر حرفه‌ای - احساس محور")
        self.root.iconbitmap("icons8-easy-listening-100.ico")
        self.root.geometry("750x600")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)

        self.current_index = 0
        self.music_list = []
        self.current_mood = None
        self.paused = False

        self.track_var = tk.StringVar()
        self.time_var = tk.StringVar()
        self.volume = tk.DoubleVar(value=0.7)

        self.setup_ui()

    def setup_ui(self):
        header_frame = tk.Frame(self.root, bg="#2c3e50")
        header_frame.pack(pady=20)

        tk.Label(header_frame, text="🎶 پخش‌کننده موزیک احساس‌محور 🎶", font=("B Nazanin", 20, "bold"),
                 fg="white", bg="#2c3e50").pack()

        mood_frame = tk.Frame(self.root, bg="#2c3e50")
        mood_frame.pack(pady=10)

        for label, mood_key in MOODS.items():
            ttk.Button(mood_frame, text=label, width=12,
                       command=lambda m=mood_key: self.load_mood(m)).pack(side="left", padx=5)

        self.listbox = tk.Listbox(self.root, font=("B Nazanin", 12), width=70, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        info_frame = tk.Frame(self.root, bg="#2c3e50")
        info_frame.pack(pady=10)

        self.track_label = tk.Label(info_frame, text="آهنگ: ", font=("B Nazanin", 12), fg="lightgreen", bg="#2c3e50")
        self.track_label.pack()

        self.artist_label = tk.Label(info_frame, text="خواننده: ", font=("B Nazanin", 12), fg="lightgreen", bg="#2c3e50")
        self.artist_label.pack()

        self.album_label = tk.Label(info_frame, text="آلبوم: ", font=("B Nazanin", 12), fg="lightgreen", bg="#2c3e50")
        self.album_label.pack()

        self.year_label = tk.Label(info_frame, text="سال ساخت: ", font=("B Nazanin", 12), fg="lightgreen", bg="#2c3e50")
        self.year_label.pack()

        self.time_label = tk.Label(info_frame, textvariable=self.time_var, font=("B Nazanin", 12), fg="lightgreen", bg="#2c3e50")
        self.time_label.pack()

        control_frame = tk.Frame(self.root, bg="#2c3e50")
        control_frame.pack(pady=15)

        ttk.Button(control_frame, text="⏮️ قبلی", command=self.prev_track).grid(row=0, column=0, padx=10)
        ttk.Button(control_frame, text="▶️ پخش", command=self.play_selected).grid(row=0, column=1, padx=10)
        ttk.Button(control_frame, text="⏸️ توقف موقت", command=self.pause).grid(row=0, column=2, padx=10)
        ttk.Button(control_frame, text="🔁 ادامه", command=self.resume).grid(row=0, column=3, padx=10)
        ttk.Button(control_frame, text="⏹️ توقف", command=self.stop).grid(row=0, column=4, padx=10)
        ttk.Button(control_frame, text="⏭️ بعدی", command=self.next_track).grid(row=0, column=5, padx=10)

        volume_frame = tk.Frame(self.root, bg="#2c3e50")
        volume_frame.pack(pady=10)
        tk.Label(volume_frame, text="🔊 صدا:", bg="#2c3e50", fg="white", font=("B Nazanin", 12)).pack(side="left")
        vol_slider = ttk.Scale(volume_frame, from_=0, to=1, orient="horizontal",
                               variable=self.volume, command=self.set_volume, length=200)
        vol_slider.pack(side="left")

    def load_mood(self, mood):
        self.music_list.clear()
        self.listbox.delete(0, tk.END)
        self.current_mood = mood

        folder = os.path.join(MOOD_DIR, mood)
        if not os.path.exists(folder):
            messagebox.showerror("خطا", f"پوشه {mood} پیدا نشد!")
            return

        for file in os.listdir(folder):
            if file.endswith(('.mp3', '.wav')):
                full_path = os.path.join(folder, file)
                metadata = get_metadata(full_path)
                self.music_list.append((file, full_path, metadata))
                self.listbox.insert(tk.END, f"{file}  ⏱️ {metadata['duration']}")

        if self.music_list:
            self.listbox.select_set(0)
            track = self.music_list[0]
            self.update_metadata_display(track)

    def play_selected(self):
        if not self.music_list:
            return
        try:
            index = self.listbox.curselection()[0]
            self.current_index = index
        except:
            index = 0
            self.current_index = 0

        track = self.music_list[index]
        self.play_music(track)

    def play_music(self, track):
        file, path, metadata = track
        try:
            mixer.music.load(path)
            mixer.music.set_volume(self.volume.get())
            mixer.music.play()
            self.track_var.set(f"🎵 در حال پخش: {file}")
            self.update_metadata_display(track)
            self.log_history(file)
        except Exception as e:
            messagebox.showerror("خطا", str(e))

    def update_metadata_display(self, track):
        _, _, metadata = track
        self.track_label.config(text=f"{metadata['title']} :آهنگ")
        self.artist_label.config(text=f"{metadata['artist']} :خواننده")
        self.album_label.config(text=f"{metadata['album']} :آلبوم")
        self.year_label.config(text=f"سال ساخت: {metadata['year']}")
        self.time_var.set(f"⏱️ مدت: {metadata['duration']}")

    def stop(self):
        mixer.music.stop()
        self.track_var.set("⏹️ موزیک متوقف شد")
        self.time_var.set("")

    def pause(self):
        mixer.music.pause()
        self.paused = True
        self.track_var.set("⏸️ توقف موقت")

    def resume(self):
        if self.paused:
            mixer.music.unpause()
            self.paused = False
            self.track_var.set("▶️ ادامه پخش")

    def next_track(self):
        if not self.music_list:
            return
        self.current_index = (self.current_index + 1) % len(self.music_list)
        self.listbox.select_clear(0, tk.END)
        self.listbox.select_set(self.current_index)
        self.play_music(self.music_list[self.current_index])

    def prev_track(self):
        if not self.music_list:
            return
        self.current_index = (self.current_index - 1) % len(self.music_list)
        self.listbox.select_clear(0, tk.END)
        self.listbox.select_set(self.current_index)
        self.play_music(self.music_list[self.current_index])

    def on_select(self, event):
        if not self.music_list:
            return
        index = self.listbox.curselection()[0]
        track = self.music_list[index]
        self.track_var.set(f"آهنگ انتخاب‌شده: {track[0]}")
        self.update_metadata_display(track)
    
    def log_history(self, track):
        with open("history.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} - {track[0]}\n")

    def set_volume(self, val):
        mixer.music.set_volume(float(val))


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()