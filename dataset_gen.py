import subprocess
command = "./fb 42 8 & ./bb 81000 -8 & ./hp 400 7 & ./mmo 1725 -17 & wait"

process = subprocess.Popen(command , stdout=subprocess.PIPE, shell = True)
proc_stdout = process.communicate()[0].strip()
print proc_stdout
