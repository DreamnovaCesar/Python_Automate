import os
import pandas as pd
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path_data_csv = r"C:\Users\Cesar\Dropbox\PC\Desktop\Excel\Data_Watchdog.xlsx"
path_to_watch = r"C:\Users\Cesar\Dropbox\PC\Desktop\Split"
Image_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Images"
Video_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Video"
Audio_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Audio"
Doc_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Documents"


Image_Exts = (".jpg", ".jpeg", ".jpe", 
            ".jif", ".jfif", ".jfi", 
            ".png", ".gif", ".webp", 
            ".tiff", ".tif", ".psd", 
            ".raw", ".arw", ".cr2", 
            ".nrw", ".k25", ".bmp", 
            ".dib", ".heif", ".heic", 
            ".ind", ".indd", ".indt", 
            ".jp2", ".j2k", ".jpf", 
            ".jpf", ".jpx", ".jpm", 
            ".mj2", ".svg", ".svgz", 
            ".ai", ".eps", ".ico")

Video_Exts = (".webm", ".mpg", ".mp2", 
            ".mpeg", ".mpe", ".mpv", 
            ".ogg", ".mp4", ".mp4v", 
            ".m4v", ".avi", ".wmv", 
            ".mov", ".qt", ".flv", 
            ".swf", ".avchd")

Audio_Exts = (".m4a", ".flac", "mp3", 
            ".wav", ".wma", ".aac")

Doc_Exts = (".doc", ".docx", ".odt",
            ".pdf", ".xls", ".xlsx", 
            ".ppt", ".pptx")
"""
def mod_csv():

    col_list = ["Name", "Size", "Folder"]
    df = pd.read_csv(path_data_csv, usecols = col_list)

    for i in range(len(Score)):
        df.loc[row, column_names[i]] = Score[i]
  
    df.to_csv(path, index = False)
  
    pd.set_option('display.max_rows', df.shape[0] + 1)
    print(df)
"""

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_file(dest, entry, name):
    if exists(str(dest) + "/" + str(name)):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        os.rename(oldName, newName)
    move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with os.scandir(path_to_watch) as entries:
            for entry in entries:
                name = entry.name
                size = os.path.getsize(entry)
                print("Name: %s, Size: %d" % (name, size))
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):  # * Checks all Audio Files
        for Audio_Ext in Audio_Exts:
            if name.endswith(Audio_Ext) or name.endswith(Audio_Ext.upper()):
                move_file(Audio_Exts, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  # * Checks all Video Files
        for Video_Ext in Video_Exts:
            if name.endswith(Video_Ext) or name.endswith(Video_Ext.upper()):
                move_file(Video_folder, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for Image_Ext in Image_Exts:
            if name.endswith(Image_Ext) or name.endswith(Image_Ext.upper()):
                move_file(Image_folder, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for Doc_Ext in Doc_Exts:
            if name.endswith(Doc_Ext) or name.endswith(Doc_Ext.upper()):
                move_file(Doc_Exts, entry, name)
                logging.info(f"Moved document file: {name}")


def main():

    logging.basicConfig(level = logging.INFO,
                        format = '%(asctime)s - %(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S')

    path = path_to_watch

    event_handler = MoverHandler()
    observer = Observer()

    observer.schedule(event_handler, path, recursive = True)
    observer.start()

    try:
        while True:
            print('Working')
            sleep(4)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()