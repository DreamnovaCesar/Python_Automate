import time
import shutil
import os
import pandas as pd

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
            ".ppt", ".pptx", ".txt",
            ".csv")

#source_path = r"C:\Users\Cesar\Dropbox\PC\Desktop\Split"
source_path = r"C:\Users\Cesar\Dropbox\PC\Downloads"
Image_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Images"
Audio_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Audio"
Video_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Video"
Doc_folder = r"C:\Users\Cesar\Dropbox\PC\Desktop\Archives\Docs"

def enumerate_files(Category, folder):

    for count, file in enumerate(os.listdir(folder)):

        filename, extension  = os.path.splitext(file)

        New_name = str(Category) + ' ' + str(count) + str(extension)

        while os.path.exists(str(folder) + "/" + str(New_name)):
            count += 1
            New_name = str(Category) + ' ' + str(count) + str(extension)

        src = folder + '/' + file  # foldername/filename, if .py file is outside folder
        dst = folder + '/' + New_name

        oldName = os.path.join(folder, file)
        newName = os.path.join(folder, New_name)

        # rename() function will
        # rename all the files
        os.rename(oldName, newName)

def Moving_files(source_path):
        with os.scandir(source_path) as files:
            for file in files:
                name = file.name
                size = os.path.getsize(file)
                print(name +  ' ' + str(size))
                Image_files(file, name)
                Audio_files(file, name)
                Video_files(file, name)
                Document_files(file, name)

def Image_files(file, name):  # * Checks all Image Files
        for Image_Ext in Image_Exts:
            if name.endswith(Image_Ext) or name.endswith(Image_Ext.upper()):
                shutil.move(file, Image_folder)

def Audio_files(file, name):  # * Checks all Audio Files
        for Audio_Ext in Audio_Exts:
            if name.endswith(Audio_Ext) or name.endswith(Audio_Ext.upper()):
                shutil.move(file, Audio_folder)

def Video_files(file, name):  # * Checks all Video Files
        for Video_Ext in Video_Exts:
            if name.endswith(Video_Ext) or name.endswith(Video_Ext.upper()):
                shutil.move(file, Video_folder)

def Document_files(file, name):  # * Checks all Document Files
        for Doc_Ext in Doc_Exts:
            if name.endswith(Doc_Ext) or name.endswith(Doc_Ext.upper()):
                shutil.move(file, Doc_folder)

def main():

    on_modified(source_path)
    enumerate_files('Image', Image_folder)
    #enumerate_files('Audio', Audio_folder)
    #enumerate_files('Video', Video_folder)
    #enumerate_files('Doc', Doc_folder)
    

if __name__ == "__main__":
    main()