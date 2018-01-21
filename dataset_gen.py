import subprocess

command = "./fib40 40 8 & ./bub5000 10000 -8 & ./hs500 500 7 & ./mat500 500 -17 & ./ms100000 100000 19 & wait"
process = subprocess.Popen(command , stdout=subprocess.PIPE, shell = True)
proc_stdout = process.communicate()[0].strip()
print proc_stdout
