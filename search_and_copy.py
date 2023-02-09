import os
import shutil

# source directory
src_dir = r"c:\source\\"
# destination directory
dst_dir = r"c:\destination\\"

# file types to be moved
xml_type = r".xml"
xls_type = r".xls"
xlsm_type = r".xlsm"

# file names (in any)
swts = r"filename_start1"
swtr = r"filename_start2"
swits = r"filename_start3"
switr = r"filename_start4"


copy_counter = 0
for path, subdirs, files in os.walk(src_dir):
    for file in files:
        if file.startswith(swts) or file.startswith(swtr) or file.startswith(swits) or file.startswith(switr):
            if file.endswith(xml_type) or file.endswith(xls_type) or file.endswith(xlsm_type):
                src = os.path.join(path, file)
                shutil.copy(src, dst_dir)
                copy_counter += 1
                print(f"Copied {src} to {dst_dir}\n")

print(f"{copy_counter} files copied")
