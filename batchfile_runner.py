import os
import subprocess


path_to_search = r"c:\temp"
file_to_search = "test.cmd"

for root, dirs, files in os.walk(path_to_search):
    for file in files:
        if file == file_to_search:
            found_file_path = os.path.join(root, file)
            print("Found ", found_file_path)
            # call the batch file
            subprocess.call(found_file_path)
            # end a MS Edge task
            os.system("taskkill /im msedge.exe /f")
