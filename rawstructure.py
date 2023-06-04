import os
import shutil 

source_dir = 'C:\Users\faisa\Desktop\file_sorter proj1'
dest_dir_pdf = 'C:\Users\faisa\Desktop\smarts\folder_pdfs'
dest_dir_txt = 'C:\Users\faisa\Desktop\smarts\folder_txt'
dest_dir_jpg = 'C:\Users\faisa\Desktop\smarts\folder_jpg'
dest_dir_png = 'C:\Users\faisa\Desktop\smarts\folder_png'
dest_dir_mp3 = 'C:\Users\faisa\Desktop\smarts\folder_mp3'

files = os.listdir(source_dir)
for file in files:
    ext = os.path.splitext(file)[1]
    source_file = os.path.join(source_dir, file)
    if ext == ".pdf":
        dest_file = os.path.join(dest_dir_pdf, file)
        if not os.path.isdir(dest_dir_pdf):
            os.mkdir(dest_dir_pdf)
        shutil.move(source_file, dest_file)