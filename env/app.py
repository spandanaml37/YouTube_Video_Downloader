import tkinter as tk
from pytube import YouTube
import customtkinter


def download(option):
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        if option == "high_quality":
            video = yt_object.streams.get_highest_resolution()
        elif option == "low_quality":
            video = yt_object.streams.get_lowest_resolution()
        elif option == "audio":
            video = yt_object.streams.get_audio_only()
        else:
            return

        title.configure(text=yt_object.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!!", text_color="green")

    except:
        finishLabel.configure(text="Download Error!!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percent_complete = bytes_download / total_size * 100
    per = str(int(percent_complete))
    progress.configure(text=per + '%')
    progress.update()

    progressbar.set(float(percent_complete) / 100)


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Link Downloader")

title = customtkinter.CTkLabel(app, text="Insert a Youtube Link", width=200, height=50, font=("cursive", 28))
title.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=50, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

download_hq = customtkinter.CTkButton(app, text="Download High Quality - Mp4", command=lambda: download("high_quality"))
download_hq.pack(padx=10, pady=10)

download_lq = customtkinter.CTkButton(app, text="Download Low Quality - Mp4", command=lambda: download("low_quality"))
download_lq.pack(padx=10, pady=10)

download_audio = customtkinter.CTkButton(app, text="Download - Mp3", command=lambda: download("audio"))
download_audio.pack(padx=10, pady=10)

app.mainloop()
