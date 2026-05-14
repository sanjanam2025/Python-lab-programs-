import os
import sys
import pathlib
import zipfile
dirName =input("Enter the directory name to backup: ")
if not os.path.isdir(dirName):
    print("directory", dirName, "does not exist.")
    sys.exit(0)
curdir=pathlib.Path(dirName)
with zipfile.ZipFile("myZip.zip",mode="w")as archieve:
    for file_path in curdir.rglob("*"):
        print(file_path)
        archieve.write(file_path)
if os.path.isfile("myZip.zip"):
    print("archieve myZip.zip created successfully.")
else:
    print("Error in creating zip archieve.")
    