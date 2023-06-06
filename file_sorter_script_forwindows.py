import os
import shutil 

source_dir = "C:\\Users\\faisa\\Desktop\\file_sorter_proj1"
dest_dir_pdf = "C:\\Users\\faisa\\Desktop\\folder_pdfs"
dest_dir_txt = "C:\\Users\\faisa\\Desktop\\folder_txt"
dest_dir_jpg = "C:\\Users\\faisa\\Desktop\\folder_jpg"
dest_dir_png = "C:\\Users\\faisa\\Desktop\\folder_png"
dest_dir_mp3 = "C:\\Users\\faisa\\Desktop\\folder_mp3"
dest_dir_py = "C:\\Users\\faisa\\Desktop\\folder_py"

files = os.listdir(source_dir)
for file in files:
    ext = os.path.splitext(file)[1]
    source_file = os.path.join(source_dir, file)
    if ext == ".pdf":
        dest_file = os.path.join(dest_dir_pdf, file)
        if not os.path.isdir(dest_dir_pdf):
            os.mkdir(dest_dir_pdf)
        shutil.move(source_file, dest_file)
    if ext == ".jpg":
        dest_file = os.path.join(dest_dir_jpg, file)
        if not os.path.isdir(dest_dir_jpg):
            os.mkdir(dest_dir_jpg)
        shutil.move(source_file, dest_file)
    if ext == ".txt":
        dest_file = os.path.join(dest_dir_txt, file)
        if not os.path.isdir(dest_dir_txt):
            os.mkdir(dest_dir_txt)
        shutil.move(source_file, dest_file)
    if ext == ".py":
        dest_file = os.path.join(dest_dir_py, file)
        if not os.path.isdir(dest_dir_py):
            os.mkdir(dest_dir_py)
        shutil.move(source_file, dest_file)
    if ext == ".png":
        dest_file = os.path.join(dest_dir_png, file)
        if not os.path.isdir(dest_dir_png):
            os.mkdir(dest_dir_png)
        shutil.move(source_file, dest_file)
    if ext == ".mp3":
        dest_file = os.path.join(dest_dir_mp3, file)
        if not os.path.isdir(dest_dir_mp3):
            os.mkdir(dest_dir_mp3)
        shutil.move(source_file, dest_file)