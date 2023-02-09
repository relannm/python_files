import os
import shutil

# source directory
src_dir = r"c:\svn\SW_VCC_PPDB\trunk\P519\\"
# destination directory
dst_dir = r"c:\Relan\Tasks\SPD_DevOps\test_files_svn\\"

# file types to be moved
xml_type = r".xml"
xls_type = r".xls"
xlsm_type = r".xlsm"

# file names (in any)
swts = r"SWTS-SW-280-1186-1187-"
swtr = r"SWTR-SW-282-1186-1187-"
swits = r"SWITS-SW-270-1186-1187-"
switr = r"SWITR-SW-272-1186-1187-"


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
