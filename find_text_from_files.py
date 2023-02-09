import os

reports_dir = r"c:\reports\\"

# read the list of reqs (with no covering objects)
print("Reading requirements (reqs.txt)")
reqs = []
f = open("reqs.txt")
reqs = f.readlines()
f.close()

# read all reports
print("Reading report files")
reports = {}
for path, subdirs, files in os.walk(reports_dir):
    for file in files:
        # do not read excel files
        if not file.endswith(".xls"):
            f = open(reports_dir + file)
            report = f.read()
            f.close()
            reports[file] = report

# find requirements in the reports
print("Searching for requirements from files")
flg_no_req_found = True
for req in reqs:
    for file in reports:
        if req in reports[file]:
            print(f'RESULT: {req} found in {file}')
            flg_no_req_found = False
            break;

if flg_no_req_found:
    print("RESULT: All requirements are missing")
